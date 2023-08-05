""" SAX core """

from __future__ import annotations

import jax
import jax.numpy as jnp

from .utils import get_params, validate_model, _replace_kwargs
from typing import (
    Dict,
    Iterable,
    Optional,
    Tuple,
)
from ._typing import (
    Model,
    SDict,
)


def circuit(
    instances: Dict[str, Model],
    connections: Dict[str, str],
    ports: Dict[str, str],
    auto_prune: bool = False,
    keep: Optional[Iterable[Tuple[str, str]]] = None,
) -> Model:
    """generate a circuit model for the instance models given

    Args:
        instances: a dictionary with as keys the model names and values
            the model dictionaries.
        connections: a dictionary where both keys and values are strings of the
            form "instancename:portname"
        ports: a dictionary mapping output portnames of the circuit to
            portnames of the form "instancename:portname".
        auto_prune: remove zero-valued connections and connections between
            non-output ports *while* evaluating the circuit SDict. This results in
            noticeably better performance and lower memory usage.  However, it also
            makes the resulting circuit non-jittable!
        keep: output port combinations to keep. All other combinations will be
            removed from the final sdict. Note: only output ports specified as
            *values* in the ports dict will be considered. For any port combination
            given, the reciprocal equivalent will automatically be added. This flag
            can be used in stead of ``auto_prune=True`` with jax.jit if you know in
            advance which port combinations of the sdict you're interested in.

    Returns:
        the circuit model with the given port names.

    Example:
        A simple mzi can be created as follows::

            import sax
            mzi = sax.circuit(
                instances = {
                    "lft": coupler_model,
                    "top": waveguide_model,
                    "btm": waveguide_model,
                    "rgt": coupler_model,
                },
                connections={
                    "lft:out0": "btm:in0",
                    "btm:out0": "rgt:in0",
                    "lft:out1": "top:in0",
                    "top:out0": "rgt:in1",
                },
                ports={
                    "lft:in0": "in0",
                    "lft:in1": "in1",
                    "rgt:out0": "out0",
                    "rgt:out1": "out1",
                },
            )
    """
    connections = {  # silently accept YAML netlist syntax
        k.replace(",", ":"): v.replace(",", ":") for k, v in connections.items()
    }
    ports = {  # silently accept YAML netlist syntax
        k.replace(",", ":"): v.replace(",", ":") for k, v in ports.items()
    }
    instances, connections, ports = validate_circuit_args(instances, connections, ports)
    if keep:
        keep_dict = {min(p1, p2): max(p1, p2) for p1, p2 in keep}
        keep = tuple((p1, p2) for p1, p2 in keep_dict.items())

    def circuit(**params):
        sdicts = {
            name: model(**params.get(name, {})) for name, model in instances.items()
        }
        return evaluate_circuit(
            sdicts, connections, ports, auto_prune=auto_prune, keep=keep
        )

    params = {name: get_params(model) for name, model in instances.items()}
    modified_circuit = _replace_kwargs(circuit, **params)

    return modified_circuit


def evaluate_circuit(
    instances: Dict[str, SDict],
    connections: Dict[str, str],
    ports: Dict[str, str],
    auto_prune: bool = False,
    keep: Optional[Iterable[Tuple[str, str]]] = None,
):
    """evaluate a circuit for the sdicts (instances) given.

    Args:
        instances: a dictionary with as keys the instance names and values
            the corresponding SDicts.
        connections: a dictionary where both keys and values are strings of the
            form "instancename:portname"
        ports: a dictionary mapping output portnames of the circuit to
            portnames of the form "instancename:portname".
        auto_prune: remove zero-valued connections and connections between
            non-output ports *while* evaluating the circuit SDict. This results in
            noticeably better performance and lower memory usage.  However, it also
            makes the resulting circuit non-jittable!
        keep: output port combinations to keep. All other combinations will be
            removed from the final sdict. Note: only output ports specified as
            *values* in the ports dict will be considered. For any port combination
            given, the reciprocal equivalent will automatically be added. This flag
            can be used in stead of ``auto_prune=True`` with jax.jit if you know in
            advance which port combinations of the sdict you're interested in.

    Returns:
        the circuit model dictionary with the given port names.

    Example:
        The SDict for a very simple mzi can for example be evaluated as follows::

            import sax
            S_mzi = sax.evaluate_circuit(
                instances = {
                    "lft": S_coupler,
                    "top": S_waveguide,
                    "rgt": S_coupler,
                },
                connections={
                    "lft:out0": "rgt:in0",
                    "lft:out1": "top:in0",
                    "top:out0": "rgt:in1",
                },
                ports={
                    "in0": "lft:in0",
                    "in1": "lft:in1",
                    "out0": "rgt:out0",
                    "out1": "rgt:out1",
                },
            )
    """
    connections = {  # silently accept YAML netlist syntax
        k.replace(",", ":"): v.replace(",", ":") for k, v in connections.items()
    }
    ports = {  # silently accept YAML netlist syntax
        k.replace(",", ":"): v.replace(",", ":") for k, v in ports.items()
    }
    ports = {v: k for k, v in ports.items()}  # it's actually easier working w reverse
    float_eps = 2 * jnp.finfo(jnp.zeros(0, dtype=float).dtype).resolution

    if keep:
        keep = set(list(keep) + [(p2, p1) for p1, p2 in keep])

    block_diag = {}
    for name, sdict in instances.items():
        block_diag.update(
            {(f"{name}:{p1}", f"{name}:{p2}"): v for (p1, p2), v in sdict.items()}
        )

    sorted_connections = sorted(connections.items(), key=_connections_sort_key)
    all_connected_instances = {k: {k} for k in instances}
    for k, l in sorted_connections:
        name1, _ = k.split(":")
        name2, _ = l.split(":")

        connected_instances = (
            all_connected_instances[name1] | all_connected_instances[name2]
        )
        for name in connected_instances:
            all_connected_instances[name] = connected_instances

        current_ports = tuple(
            p
            for instance in connected_instances
            for p in set([p for p, _ in block_diag] + [p for _, p in block_diag])
            if p.startswith(f"{instance}:")
        )

        block_diag.update(_interconnect_ports(block_diag, current_ports, k, l))

        for i, j in list(block_diag.keys()):
            is_connected = i == k or i == l or j == k or j == l
            is_in_output_ports = i in ports and j in ports
            if is_connected and not is_in_output_ports:
                del block_diag[i, j]  # we're not interested in these port combinations

    if auto_prune:
        circuit_sdict = {
            (ports[i], ports[j]): v
            for (i, j), v in block_diag.items()
            if i in ports and j in ports and jnp.any(jnp.abs(v) > float_eps)
        }
    elif keep:
        circuit_sdict = {
            (ports[i], ports[j]): v
            for (i, j), v in block_diag.items()
            if i in ports and j in ports and (ports[i], ports[j]) in keep
        }
    else:
        circuit_sdict = {
            (ports[i], ports[j]): v
            for (i, j), v in block_diag.items()
            if i in ports and j in ports
        }
    return circuit_sdict


def _connections_sort_key(connection):
    """sort key for sorting a connection dictionary

    Args:
        connection of the form '{instancename}:{portname}'
    """
    part1, part2 = connection
    name1, _ = part1.split(":")
    name2, _ = part2.split(":")
    return (min(name1, name2), max(name1, name2))


def _interconnect_ports(block_diag, current_ports, k, l):
    """interconnect two ports in a given model

    Args:
        model: the component for which to interconnect the given ports
        k: the first port name to connect
        l: the second port name to connect

    Returns:
        the resulting interconnected component, i.e. a component with two ports
        less than the original component.

    Note:
        The interconnect algorithm is based on equation 6 in the paper below::

          Filipsson, Gunnar. "A new general computer algorithm for S-matrix calculation
          of interconnected multiports." 11th European Microwave Conference. IEEE, 1981.
    """
    current_block_diag = {}
    for i in current_ports:
        for j in current_ports:
            vij = _calculate_interconnected_value(
                vij=block_diag.get((i, j), 0.0),
                vik=block_diag.get((i, k), 0.0),
                vil=block_diag.get((i, l), 0.0),
                vkj=block_diag.get((k, j), 0.0),
                vkk=block_diag.get((k, k), 0.0),
                vkl=block_diag.get((k, l), 0.0),
                vlj=block_diag.get((l, j), 0.0),
                vlk=block_diag.get((l, k), 0.0),
                vll=block_diag.get((l, l), 0.0),
            )
            current_block_diag[i, j] = vij
    return current_block_diag


@jax.jit
def _calculate_interconnected_value(vij, vik, vil, vkj, vkk, vkl, vlj, vlk, vll):
    """Calculate an interconnected S-parameter value

    Note:
        The interconnect algorithm is based on equation 6 in the paper below::

          Filipsson, Gunnar. "A new general computer algorithm for S-matrix calculation
          of interconnected multiports." 11th European Microwave Conference. IEEE, 1981.
    """
    result = vij + (
        vkj * vil * (1 - vlk)
        + vlj * vik * (1 - vkl)
        + vkj * vll * vik
        + vlj * vkk * vil
    ) / ((1 - vkl) * (1 - vlk) - vkk * vll)
    return result


def validate_circuit_args(
    instances: Dict[str, Model], connections: Dict[str, str], ports: Dict[str, str]
) -> Tuple[Dict[str, Model], Dict[str, str], Dict[str, str]]:
    """validate the netlist parameters of a circuit

    Args:
        instances: a dictionary with as keys the model names and values
            the model dictionaries.
        connections: a dictionary where both keys and values are strings of the
            form "instancename:portname"
        ports: a dictionary mapping output portnames of the circuit to
            portnames of the form "instancename:portname".

    Returns:
        the validated and possibly slightly modified instances, connections and
        ports dictionaries.
    """

    for name, model in instances.items():
        validate_model(model)

    if not isinstance(connections, dict):
        msg = f"Connections should be a str:str dict or a list of length-2 tuples."
        connections, _connections = {}, connections
        connection_ports = set()
        for conn in _connections:
            connections[conn[0]] = conn[1]
            for port in conn:
                msg = f"Duplicate port found in connections: '{port}'"
                assert port not in connection_ports, msg
                connection_ports.add(port)

    connection_ports = set()
    for connection in connections.items():
        for port in connection:
            msg = f"Connection ports should all be strings. Got: '{port}'"
            assert isinstance(port, str), msg
            msg = f"Connection ports should have format 'modelname:port'. Got: '{port}'"
            assert len(port.split(":")) == 2, msg
            name, _ = port.split(":")
            msg = f"Model '{name}' used in connection "
            msg += f"'{connection[0]}':'{connection[1]}', "
            msg += f"but '{name}' not found in instances dictionary."
            assert name in instances, msg
            msg = f"Duplicate port found in connections: '{port}'"
            assert port not in connection_ports, msg
            connection_ports.add(port)

    output_ports = set()
    for output_port, port in ports.items():
        msg = f"Ports keys in 'ports' should all be strings. Got: '{port}'"
        assert isinstance(port, str), msg
        msg = f"Port values in 'ports' should all be strings. Got: '{output_port}'"
        assert isinstance(output_port, str), msg
        msg = f"Port values in 'ports' should have format 'model:port'. Got: '{port}'"
        assert len(port.split(":")) == 2, msg
        msg = f"Port keys in 'ports' shouldn't contain a ':'. Got: '{output_port}'"
        assert ":" not in output_port, msg
        msg = f"Duplicate port found in ports or connections: '{port}'"
        assert port not in connection_ports, msg
        name, _ = port.split(":")
        msg = f"Model '{name}' used in output port "
        msg += f"'{port}':'{output_port}', "
        msg += f"but '{name}' not found in instances dictionary."
        assert name in instances, msg
        connection_ports.add(port)
        msg = f"Duplicate port found in output ports: '{output_port}'"
        assert output_port not in output_ports, msg
        output_ports.add(output_port)

    return instances, connections, ports

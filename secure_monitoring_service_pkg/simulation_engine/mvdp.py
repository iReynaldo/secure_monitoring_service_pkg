import copy
from collections import Counter

import igraph as ig
from igraph import plot
import numpy as np

from secure_monitoring_service_pkg.simulation_framework.sim_logger import test_logger as logger
from secure_monitoring_service_pkg.simulation_framework import sim_logger


################################
# Functions
################################

def asn_set_from_edge_list(edge_list):
    # Get count of number of unique ASes
    asn_set = set()
    for edge in edge_list:
        asn_set.add(edge[0])
        asn_set.add(edge[1])
    return asn_set


def asn_set_from_path_list(path_list):
    # Get count of number of unique ASes
    asn_set = set()
    for path in path_list:
        asn_set.update(path)
    return asn_set

def target_asn_set_from_path_list(path_list, max_number_of_dishonest_nodes):
    """
    Returns a reduced list of target asns based on whether or not they
    mininumally show up in 'max_number_of_dishonest_nodes' paths in
    :param path_list:
    :param max_number_of_dishonest_nodes:
    :return:
    """
    asn_set = set()
    asn_counter = Counter()
    for path in path_list:
        for asn in path:
            # TODO: if there's a case where an ASN is added to the same path multiple times,
            # this doesn't account fo that. It assumes this kind of manipulation is not part of our
            # simulations. Adding it is simple, but want to keep this as lean as possible.
            asn_counter[asn] += 1
            if asn_counter[asn] > max_number_of_dishonest_nodes:
                asn_set.add(asn)
    return asn_set


def map_asns_to_seq(path_list):
    """
    Mutates the passed in path_list and returns a dict of mapping
    :param path_list:
    :return:
    """
    asn_seq_map = dict()  # (key, value) = (asn, seq_value)
    seq_asn_map = dict()  # (key, value) = (seq_value, asn)
    seq_num = 0
    for i, path in enumerate(path_list):
        for j, asn in enumerate(path):
            if asn in asn_seq_map:
                path_list[i][j] = asn_seq_map[path_list[i][j]]
            else:
                asn_seq_map[asn] = seq_num
                seq_asn_map[seq_num] = asn
                path_list[i][j] = asn_seq_map[path_list[i][j]]
                seq_num += 1
    return (seq_asn_map, asn_seq_map)


def create_report_graph_object_with_capacities(edge_list):
    """
    For a edge_list create the graph object, and
    consider which ASes are adopters.
    :param edge_list:
    :return:
    """
    # Generate the graph with its capacities
    number_of_ases = len(asn_set_from_edge_list(edge_list))

    # Create graph object
    g = ig.Graph(
        number_of_ases,
        edge_list,
        directed=True
    )

    logger.debug("Graph edge list: {0}".format(edge_list))

    # Add edge capacities to graph
    capacity_list = [1] * len(edge_list)
    g.es["capacity"] = capacity_list  # capacity of each edge

    return g


def paths_to_edge_list(path_list):
    """
    For a given prefix, return the edge list
    for the associated list of reports.
    """
    edge_set = set()  # Will be a set of tuples
    for path in path_list:
        path_length = len(path)
        # Extract edge list from path
        for i in range(path_length - 1):
            edge_set.add((path[i], path[i + 1]))
    return list(edge_set)


def create_vin_vout_vertices(path_list):
    # Convert paths
    # (i.e. each nodes must be split into v_in and v_out)
    # v_in will be the negative of v_out
    # For example:
    # Input:  [1, 2, 3]
    # Output: [-1, 1, -2, 2, -3, 3]
    converted_target_asn_path_list = list()
    for path in path_list:
        converted_path = list()
        for asn in path:
            converted_path.append(asn)
            converted_path.append(asn * -1)
        converted_target_asn_path_list.append(converted_path)
    return converted_target_asn_path_list


def get_mvdp_with_subgraph_pictures(path_list, target_asn):
    """
    TODO: Complete Documentation

    Use this method only for debugging. Not used for simulations.
    :param path_list:
    :param target_asn:
    :param k: maximum number of dishonest nodes
    :return:
    """
    path_list_copy = copy.deepcopy(path_list)
    logger.debug("Path List: {0}".format(path_list_copy))

    # Get list of paths that include target_asn
    target_asn_path_list = list()
    for path in path_list_copy:
        if target_asn in path:
            path_to_target_asn = path[:path.index(target_asn) + 1]
            target_asn_path_list.append(path_to_target_asn)

    # Create v_in and v_out vertices
    converted_target_asn_path_list = create_vin_vout_vertices(path_list_copy)

    # Remap asns to sequence
    (seq_asn_map, asn_seq_map) = map_asns_to_seq(converted_target_asn_path_list)
    logger.debug("Remapped Converted target asn path list: {0}".format(converted_target_asn_path_list))

    # Create artificial source edges
    artificial_source_asn = max(seq_asn_map) + 1
    seq_asn_map[artificial_source_asn] = artificial_source_asn
    asn_seq_map[artificial_source_asn] = artificial_source_asn
    source_edge_set = set()
    for path in converted_target_asn_path_list:
        source_edge_set.add((artificial_source_asn, path[0]))
    source_edge_list = list(source_edge_set)

    # Create graph edge list
    graph_edge_list = paths_to_edge_list(converted_target_asn_path_list)
    graph_edge_list.extend(source_edge_list)

    # Create graph
    report_graph = create_report_graph_object_with_capacities(graph_edge_list)

    # Run the max flow
    adjusted_target = asn_seq_map[target_asn]
    logger.debug("Artificial Source: {0}".format(artificial_source_asn))
    logger.debug("Adjusted Target: {0}".format(adjusted_target))
    flow = report_graph.maxflow(source=artificial_source_asn,
                                target=adjusted_target,
                                capacity=report_graph.es["capacity"]
                                )

    logger.debug("Capacities: {0}".format(report_graph.es["capacity"]))
    logger.debug("Max flow: {0}".format(flow.value))
    logger.debug("Edge assignments: {0}".format(flow.flow))

    for v in report_graph.vs:
        v["label"] = seq_asn_map[v.index]
    layout = report_graph.layout("kk")
    plot(report_graph, "plot.png", layout=layout)

    return flow.value


def create_report_graph(path_list):
    """
    TODO: Complete Documentation

    :param path_list:
    :param target_asn:
    :param k: maximum number of dishonest nodes
    :return:
    """
    # Create v_in and v_out vertices
    converted_path_list = create_vin_vout_vertices(path_list)

    # Remap asns to sequence
    (seq_asn_map, asn_seq_map) = map_asns_to_seq(converted_path_list)
    logger.debug("Remapped Converted path list: {0}".format(converted_path_list))

    # Create graph edge list
    graph_edge_list = paths_to_edge_list(converted_path_list)

    # Create graph
    prelim_report_graph = create_report_graph_object_with_capacities(graph_edge_list)

    # Identify the leaves
    # Leaves should have 0 in-degree
    nparray_of_leaf_vector_ids = np.where(np.array(prelim_report_graph.degree(mode="in")) == 0)[0]
    del prelim_report_graph

    # Create artificial source edges
    artificial_source_asn = max(seq_asn_map) + 1
    seq_asn_map[artificial_source_asn] = 0
    asn_seq_map[0] = artificial_source_asn
    source_edge_set = set()
    for leaf in nparray_of_leaf_vector_ids:
        source_edge_set.add((artificial_source_asn, leaf))
    source_edge_list = list(source_edge_set)

    # TODO: Recreate graph with artificial source added  / Add artificial source to existing graph
    # TODO: Which way is faster?
    # Add artificial source edges to graph edge list
    graph_edge_list.extend(source_edge_list)

    # Recreate graph with newly added source edges
    logger.debug("Added Artificial Source to Graph Edge List")
    report_graph = create_report_graph_object_with_capacities(graph_edge_list)

    return report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, nparray_of_leaf_vector_ids


def get_max_vdp(report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, target_asn, plot_graph=False):
    # Run the max flow
    adjusted_target = asn_seq_map[target_asn]
    logger.debug("Artificial Source: {0}".format(artificial_source_asn))
    logger.debug("Adjusted Target: {0}".format(adjusted_target))
    flow = report_graph.maxflow(source=artificial_source_asn,
                                target=adjusted_target,
                                capacity=report_graph.es["capacity"]
                                )

    if plot_graph:
        logger.debug("Capacities: {0}".format(report_graph.es["capacity"]))
        logger.debug("Max flow: {0}".format(flow.value))
        logger.debug("Edge assignments: {0}".format(flow.flow))
        for v in report_graph.vs:
            v["label"] = seq_asn_map[v.index]
        layout = report_graph.layout("kk")
        plot(report_graph, f"report_graph_targe_asn_{target_asn}.png", layout=layout)

    return flow.value

# @profile
def get_avoid_list(reports_path_list, max_num_dishonest_nodes):
    logger.debug("Reports Path List: {0}".format(reports_path_list))
    target_asn_set = target_asn_set_from_path_list(reports_path_list, max_num_dishonest_nodes)
    avoid_list = list()
    (report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, nparray_of_leaf_vector_ids) = create_report_graph(reports_path_list)
    for target_asn in target_asn_set:
        # Optimization: Calculate mvdp only if it's not a leaf
        if asn_seq_map[target_asn] not in nparray_of_leaf_vector_ids:
            max_num_vdp = get_max_vdp(report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, target_asn, sim_logger.CONDUCTING_SYSTEM_TEST)
            if max_num_vdp > max_num_dishonest_nodes:
                avoid_list.append(target_asn)
    logger.debug("Avoid List: {0}".format(avoid_list))
    return avoid_list




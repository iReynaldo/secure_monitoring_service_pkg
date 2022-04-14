import igraph as ig
from igraph import plot
import copy


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


def create_report_graph(edge_list):
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

    print("Graph edge list", edge_list)

    # Add edge capacities to graph
    capacity_list = list()
    for i in range(len(edge_list)):
        capacity_list.append(1)
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
        for i in range(path_length-1):
            edge_set.add((path[i], path[i + 1]))
    return list(edge_set)


def get_max_number_of_vertex_disjoint_paths(path_list, target_asn):
    """

    :param path_list:
    :param target_asn:
    :param k: maximum number of dishonest nodes
    :return:
    """
    path_list_copy = copy.deepcopy(path_list)
    print("Path List: ", path_list_copy)

    # Get list of paths that include target_asn
    target_asn_path_list = list()
    for path in path_list_copy:
        if target_asn in path:
            path_to_target_asn = path[:path.index(target_asn)+1]
            target_asn_path_list.append(path_to_target_asn)

    # TODO: move to its own function
    # Convert paths
    # (i.e. each nodes must be split into v_in and v_out)
    # v_in will be the negative of v_out
    # For example:
    # Input:  [1, 2, 3]
    # Output: [-1, 1, -2, 2, -3, 3]
    converted_target_asn_path_list = list()
    for path in target_asn_path_list:
        converted_path = list()
        for asn in path:
            converted_path.append(asn*-1)  # TODO: Change This will only work for small test
            converted_path.append(asn)
        converted_target_asn_path_list.append(converted_path)
    print("Converted target asn path list: ", converted_target_asn_path_list)

    # Remap asns to sequence
    (seq_asn_map, asn_seq_map) = map_asns_to_seq(converted_target_asn_path_list)
    print("Remapped Converted target asn path list: ", converted_target_asn_path_list)

    # TODO: move to its own function
    # Create artificial source edges
    artificial_source_asn = max(seq_asn_map)+1
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
    report_graph = create_report_graph(graph_edge_list)

    # Run the max flow
    adjusted_target = asn_seq_map[target_asn*-1]
    print("Artificial Source: ", artificial_source_asn)
    print("Adjusted Target: ", adjusted_target)
    flow = report_graph.maxflow(source=artificial_source_asn,
                                target=adjusted_target,
                                capacity=report_graph.es["capacity"]
                                )

    # TODO: Remove lines after debugging
    print("Capacities", report_graph.es["capacity"])
    print("Max flow:", flow.value)
    print("Edge assignments:", flow.flow)

    for v in report_graph.vs:
        v["label"] = seq_asn_map[v.index]
    layout = report_graph.layout("kk")
    plot(report_graph, layout=layout)

    return flow.value


def get_suspects(reports_path_list, max_num_dishonest_nodes):
    asn_set = asn_set_from_path_list(reports_path_list)
    suspects = list()
    for target_asn in asn_set:
        max_num_vdp = get_max_number_of_vertex_disjoint_paths(reports_path_list, target_asn)
        if max_num_vdp > max_num_dishonest_nodes:
            suspects.append(target_asn)
    print("Suspects: ", suspects)
    return suspects

# TODO: quick test of functions


reports_path_list = [
    [10, 3, 2, 1],
    [20, 3, 2, 1],
    [30, 4, 2, 1],
    [40, 5, 1]
]
# get_max_number_of_vertex_disjoint_paths(reports_path_list, 1)
get_suspects(reports_path_list, 1)

# reports_path_list = [
#      [2, 4, 5, 7],
#      [3, 4, 6, 7]
# ]
# get_number_of_vertex_disjoint_paths(reports_path_list, 7)

# reports_path_list = [
#     [1, 3],
#     [2, 3],
# ]
# get_number_of_vertex_disjoint_paths(reports_path_list, 3)

# Mapper Test
#-------------------------------------------------
# reports_path_list = [
#     [999, 222],
#     [4444, 222],
# ]
# the_map = map_asns_to_seq(reports_path_list)
# print(reports_path_list)
# print(the_map)
#-------------------------------------------------



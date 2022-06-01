from lib_secure_monitoring_service import mvdp



def test_essentials_3_nodes():
    reports_path_list = [
        [10, 3],
        [20, 3],
    ]
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 3)
    (report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, nparray_of_leaf_vector_ids) = mvdp.create_report_graph(reports_path_list)
    flow_value = mvdp.get_max_vdp(report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, 3)
    assert flow_value == 2


def test_essentials_6_nodes():
    reports_path_list = [
         [2, 4, 5, 7],
         [3, 4, 6, 7]
    ]
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 7)
    (report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, nparray_of_leaf_vector_ids) = mvdp.create_report_graph(reports_path_list)
    flow_value = mvdp.get_max_vdp(report_graph, seq_asn_map, asn_seq_map, artificial_source_asn, 7)
    assert flow_value == 1


def test_essentials_9_nodes_k1():
    """
    k = 1
    :return:
    """
    reports_path_list = [
        [10, 3, 2, 1],
        [20, 3, 2, 1],
        [30, 4, 2, 1],
        [40, 5, 1]
    ]
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    avoid_list = mvdp.get_avoid_list(reports_path_list, 1)
    expected_avoid_set = {1, 2, 3}
    assert set(avoid_list) == expected_avoid_set


def test_essentials_9_nodes_k2():
    """
    k = 1
    :return:
    """
    reports_path_list = [
        [10, 3, 2, 1],
        [20, 3, 2, 1],
        [30, 4, 2, 1],
        [40, 5, 1]
    ]
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    avoid_list = mvdp.get_avoid_list(reports_path_list, 2)
    expected_avoid_set = set()
    assert set(avoid_list) == expected_avoid_set


def test_k1_with_adopters_in_report_paths():
    """
    k = 1
    :return:
    """
    # In this one you can see that 2 reports [2, 1]
    # 2 is already part of many reported paths.
    # 2 should not be considered a leaf in the report graph
    # The report graph of this should look the same as seen in test_essentials_9_nodes_k1
    reports_path_list = [
        [10, 3, 2, 1],
        [20, 3, 2, 1],
        [30, 4, 2, 1],
        [40, 5, 1],
        [2, 1]
    ]
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    avoid_list = mvdp.get_avoid_list(reports_path_list, 1)
    expected_avoid_set = {1, 2, 3}
    assert set(avoid_list) == expected_avoid_set


if __name__ == "__main__":
    test_essentials_3_nodes()
    test_essentials_6_nodes()
    test_essentials_9_nodes_k1()
    test_essentials_9_nodes_k2()
    test_k1_with_adopters_in_report_paths()

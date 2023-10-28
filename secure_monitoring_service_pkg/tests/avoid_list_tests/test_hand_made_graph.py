import igraph as ig

# Imported for debugging code at the bottom


def test_hand_made_graph():
    # Graph
    """
      2   5
     / \ / \
    1   4   7
     \ / \ /
      3   6
    """
    # Generate the graph with its capacities
    # Note the below graph doesn't follow the rule used in mvdp.py for making v_in and v_out
    g = ig.Graph(
        14,
        [
            (101, 1),
            (1, 102),
            (1, 103),
            (102, 2),
            (2, 104),
            (103, 3),
            (3, 104),
            (104, 4),
            (4, 105),
            (4, 106),
            (105, 5),
            (5, 107),
            (106, 6),
            (6, 107),
            (107, 7),
        ],
        directed=True,
    )
    g.es["capacity"] = [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]  # capacity of each edge

    # For debugging purposes you can try different sources and sinks from command line
    # source1 = int(sys.argv[1]) 1
    # target1 = int(sys.argv[2]) 104

    source1 = 1
    target1 = 104

    # Run the max flow
    flow = g.maxflow(source=source1, target=target1, capacity=g.es["capacity"])

    assert flow.value == 2.0

    # The following are for debugging purposes
    # Uncomment to see detailed results
    #
    # print("Max flow:", flow.value)
    # print("Edge assignments:", flow.flow)
    #
    # for v in g.vs:
    #     v["label"] = str(v.index)
    # layout = g.layout("kk")
    # plot(g, layout=layout)


if __name__ == "__main__":
    test_hand_made_graph()

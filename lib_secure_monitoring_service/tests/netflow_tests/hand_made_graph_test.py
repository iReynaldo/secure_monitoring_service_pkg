import igraph as ig
from igraph import plot
import matplotlib.pyplot as plt
import sys

# Graph
"""
  2   5
 / \ / \
1   4   7
 \ / \ /
  3   6
"""
# Generate the graph with its capacities
g = ig.Graph(
            14,
            [(101, 1), (1, 102), (1, 103),
             (102, 2), (2, 104),
             (103, 3), (3, 104),
             (104, 4), (4, 105), (4, 106),
             (105, 5), (5, 107),
             (106, 6), (6, 107),
             (107, 7)],
            directed=True
        )
g.es["capacity"] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # capacity of each edge

source1 = int(sys.argv[1])
target1 = int(sys.argv[2])

# Run the max flow
flow = g.maxflow(source=source1, target=target1, capacity=g.es["capacity"])

print("Max flow:", flow.value)
print("Edge assignments:", flow.flow)

for v in g.vs:
    v["label"] = str(v.index)
layout = g.layout("kk")
plot(g, layout=layout)

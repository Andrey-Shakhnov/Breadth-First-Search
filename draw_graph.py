import networkx as nx
import time
import pylab as plt
import os

g = nx.Graph()
nodes = [0,1,2,3,4,5]

for i in nodes:
    g.add_node(i)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)

nx.draw(g, with_labels=True)
plt.savefig("plot.png")
plt.show()

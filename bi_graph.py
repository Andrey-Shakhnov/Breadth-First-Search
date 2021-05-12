import networkx as nx
import random
import time
import numpy as np
import matplotlib.pyplot as plot
import pylab as plt
from plot_builder import time_counter

data_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 2500]
data_test = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
data_t = []


def generate_bigraph(n):
    sides = dict()
    sides[1] = []
    sides[2] = []
    keys = sides.keys()
    for k in range(0, n):
        node = random.randint(1, 2)
        #if len(sides[node]) == n // 2:
        #for j in keys:
            #if j != node:
                #sides[j].append(k)
    #else:
        sides[node].append(k)

    g = nx.Graph()

    for q in sides[1]:
        for j in sides[2]:
            g.add_edge(q, j)

    return g

for n in data_n:
    a = []
    for i in range(10):
        graph = generate_bigraph(n)
        time = time_counter(graph)
        a.append(time)
    print(a)
    t = np.sum(a)
    print("sum = ", t)
    print("average = ", t/10)
    data_t.append(t/10)
    print(data_t)
    #data_t = sorted(data_t)


plot.plot(data_t, data_n)
plot.ylabel('Vertex')
plot.xlabel('Time')
plot.show()

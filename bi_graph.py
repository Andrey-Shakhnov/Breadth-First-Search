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

    """end = 1
    eccentricity = dict()
    lens = []

    isolate = list(nx.isolates(g))
    if isolate:
        for i in isolate:
            g.add_edge(i, end)

    for i in range(n - 1):
        if end in isolate:
            end += 1
        else:
            start = 0
            p = nx.shortest_path(g, source=0, target=end)
            end += 1
            if len(p) in eccentricity:
                eccentricity[len(p)].append(p)
            else:
                eccentricity[len(p)] = []
                eccentricity[len(p)].append(p)
                lens.append(len(p))

    max_len = max(lens)
    print("Eccentricity of 0 vertex is:", max_len - 1)
    print(eccentricity[max_len])

    eccentricity_keys = eccentricity.keys()

    nx.draw(g, with_labels=True)
    plt.savefig("plot.png")
    plt.show()

    cent = nx.center(g)
    print("Center - ", cent)
    diam = nx.diameter(g)
    print("Diameter - ", diam)
    rad = nx.radius(g)
    print("Radius - ", rad)"""

    #nx.draw(g, with_labels=True)
    #plt.savefig("plot.png")
    #plt.show()

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

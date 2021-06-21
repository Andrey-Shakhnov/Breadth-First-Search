import networkx as nx
import random
import time
import numpy as np
import matplotlib.pyplot as plot
import pylab as plt
from cycler import cycler
from time_counter import time_counter

data_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
data_t = []


def generate_splitgraph(n):
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
        if k == n-1:
            if not sides[2]:
                sides[2].append(k)
            elif len(sides[2]) == n-1:
                sides[1].append(k)
            else:
                sides[node].append(k)
        else:
            sides[node].append(k)

    g = nx.Graph()

    for new_node in sides[1]:
        g.add_node(new_node)
    for new_node in sides[2]:
        g.add_node(new_node)

    for q in sides[1]:
        for j in sides[2]:
            probability = random.random()
            if probability <= 0.9:
                g.add_edge(q, j)

    for l in sides[1]:
        for e in sides[1]:
            g.add_edge(l, e)

    isolate = list(nx.isolates(g))
    for node in isolate:
        if node in sides[2]:
            g.add_edge(node, sides[1][0])

    return g
def eccent(g):
    end = 1
    eccentricity = dict()
    lens = []

    isolate = list(nx.isolates(g))
    if isolate:
        for i in isolate:
            g.add_edge(i, end)

    for i in range(n - 1):
        start = 0
        p = nx.shortest_path(g, source=0, target=end)
        end += 1
        if len(p) in eccentricity:
            eccentricity[len(p)].append(p)
        else:
            eccentricity[len(p)] = []
            eccentricity[len(p)].append(p)
            lens.append(len(p))

    max_len = max(lens) - 1


    return max_len
d = dict()
for n in data_n:
    a = []
    d[n] = list()
    for i in range(10):
        graph = generate_splitgraph(n)
        ewa = eccent(graph)
        time = time_counter(graph)
        a.append(time)
        d[n].append(ewa)
    print(a)
    print(d)
    t = np.sum(a)
    print("sum = ", t)
    print("average = ", t/10)
    data_t.append(t/10)
    print(data_t)
    #data_t = sorted(data_t)


data_to_dataset =  str(data_t) + "\n" + str(data_n) + "\n"
data_path = str(d) + "\n"
with open("dataset.txt", "a") as file:
    file.write(data_to_dataset)
with open("dataset_ways.txt", "a") as file:
    file.write(data_path)

#plot.title('Chart price', fontsize=17)
#plot.plot(data_t, data_n, label='first')
#plot.legend()
#plot.ylabel('Vertex')
#plot.xlabel('Time')
#plot.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plot
from time_counter import time_counter

data_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
data_t = []

flag = 0
check = 0


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

    average_len = sum(lens)/len(lens)

    return average_len

d = dict()
for n in data_n:
	p = 1
	a = []
	d[n] = list()
	for u in range(10):
		G = nx.fast_gnp_random_graph(n, p)
		#root = 0
		#nx.write_edgelist(G, 'edge_list2.txt')
		#G3 = nx.read_edgelist('edge_list2.txt')
		#A = nx.adjacency_matrix(G)
		#start_time = time.time()
		#G4 = nx.Graph(A)
		#nx.bfs_edges(G4,0)
	#start_time = time.time()
		#nx.write_edgelist(G,'edge_list2.txt')
		#edges = nx.bfs_edges(G,root)
	#nx.bfs_edges(G3,0)
	#nodes = [root] + [v for u, v in edges]
		time = time_counter(G)
		ewa = eccent(G)
		a.append(time)
		d[n].append(ewa)
	print(a)
	print(d)
	t = np.sum(a)
	print("sum = ", t)
	print("average = ", t / 10)
	data_t.append(t / 10)
	print(data_t)

data_to_dataset = str(data_t) + "\n" + str(data_n) + "\n"
data_path = str(d) + "\n"
with open("dataset.txt", "a") as file:
	file.write(data_to_dataset)
with open("dataset_ways.txt", "a") as file:
	file.write(data_path)
plot.plot(data_t,data_n)
plot.ylabel('Vertex')
plot.xlabel('Time')
plot.show()

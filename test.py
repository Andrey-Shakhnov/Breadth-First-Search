import networkx as nx
import time
import numpy as np
import matplotlib.pyplot as plot

data_n = [100,200,300,400,500,600,700,800,900,1000,2000,2500]
data_t = []

flag = 0
check = 0
while (check != 12):
	n = int(input("Enter quantity of Vertex: "))
	p = 0.7
	a = []
	for i in range(12):
		G = nx.fast_gnp_random_graph(n,p)
		#root = 0	
		#nx.write_edgelist(G,'edge_list2.txt')
		#G3 = nx.read_edgelist('edge_list2.txt')
		A = nx.adjacency_matrix(G)
		start_time = time.time()
		G4 = nx.Graph(A)
		nx.bfs_edges(G4,0)
		#nx.write_edgelist(G,'edge_list2.txt')
		#edges = nx.bfs_edges(G,root)
		#nx.bfs_edges(G3,0)
		#nodes = [root] + [v for u, v in edges]
		times = time.time() - start_time
		a.append(times)
	print(a)
	t = np.sum(a)
	print("sum = ",t)
	data_t.append(t)
	print(data_t)
	data_t = sorted(data_t)
	check+=1
	#print("Do u want another quantity of Vertex? ")
	#key = input("y/n? \n")
	#if (key == "y"):
		#flag = 0
	#else: 
		#flag = 1

plot.plot(data_t,data_n)
plot.ylabel('Vertex')
plot.xlabel('Time')
plot.show()

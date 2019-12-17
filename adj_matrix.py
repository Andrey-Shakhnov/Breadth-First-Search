import networkx as nx
import time
import pylab as plt

n = int(input("Enter vertex "))
p = 0.5
G1 = nx.fast_gnp_random_graph(n,p)
#nx.write_edgelist(G1,'edge_list2.txt')

A = nx.adjacency_matrix(G1)
G4 = nx.Graph(A)
time.perf_counter()
nx.bfs_edges(G4,0)
times = time.process_time()
print("BFS time is: ",time.process_time()," seconds")
print(nx.info(G4))

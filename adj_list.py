import networkx as nx
import time
import pylab as plt

n = int(input("Enter vertex "))
p = 0.5
G1 = nx.fast_gnp_random_graph(n,p)
nx.write_edgelist(G1,'edge_list2.txt')

G3 = nx.read_edgelist('edge_list2.txt')
time.perf_counter()
nx.bfs_edges(G3,0)
times = time.process_time()	


print(nx.info(G3))

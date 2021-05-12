import networkx as nx
import random
import time
import numpy as np
import matplotlib.pyplot as plot



def time_counter(graph):
    root = 0
    start_time = time.time()
    edges = nx.bfs_edges(graph, root)
    nodes = [root] + [v for u, v in edges]
    times = time.time() - start_time
    return times

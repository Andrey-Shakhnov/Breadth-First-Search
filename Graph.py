import networkx as nx
import time
import pylab as plt
import os

launch = True
while (launch == True):
	n = int(input("Enter quantity of Vertex: "))
	p = float(input("Enter probabiluty of edge: "))

	#Генерируем рандомный граф
	G = nx.fast_gnp_random_graph(n,p)

	print(G)
	#Выполняем поиск в ширину и считаем время, за которое он производится
	root = 0
	time.perf_counter()
	edges = nx.bfs_edges(G,root)
	nodes = [root] + [v for u, v in edges]
	times = time.process_time()
	print("BFS time is: ",time.process_time()," seconds")
	
	#Вывести путь поиска в ширину?
	if (n <= 20):
		print("The BFS way is: \n",nodes)
	else:
		print("Do you want to see BFS way?")
		key1 = input("y/n? \n")
		if (key1 == "y"):
			print(nodes)

	#При количестве вершин <= 15 нарисовать граф, иначе выдать запрос на рисование.
	if (n <=15):
		nx.draw(G, with_labels = True)
		plt.savefig("plot.png")
		plt.show()
	else:
		print("Draw it?")
		keyDraw = input("y/n? ")
		if (keyDraw == "y"):
			nx.draw(G, with_labels = True)
			plt.savefig("plot.png")
			plt.show()

	#Спросить, нужно ли добавить ребра, если да, то сколько. 
	print("Do you want to add any edges?")
	keyadd = input("y/n? ")
	if (keyadd == "y"):
		val = int(input("How many edges need to add? "))
		for i in range(val):
			startV = int(input("Enter start vertex "))
			endV = int(input("Enter end vertex "))
			G.add_edges_from([(startV, endV)]) #Добавляем ребро от вершины startV к вершине endV.
	print("==========================================")
	
	#Кратчайшие пути: от введенной вершины до всех остальных и от нулевой до введённой
	end = 1
	eccentricity = dict()
	lens = []

	isolate = list(nx.isolates(G))
	if isolate:
		for i in isolate:
			G.add_edge(i, end)

	for i in range(n-1):
		if end in isolate:
			end+=1
		else:
			start = 0
			p = nx.shortest_path(G,source = 0, target = end)
			end+=1
			if len(p) in eccentricity:
				eccentricity[len(p)].append(p)
			else:
				eccentricity[len(p)] = []
				eccentricity[len(p)].append(p)
				lens.append(len(p))

	max_len = max(lens)
	print("Eccentricity of 0 vertex is:", max_len - 1)
	print(eccentricity[max_len])

	ddd = eccentricity.keys()

	if (n<=500):
		print("Find center?")
		key4 = input("y/n?")
		if (key4 == "y"):
			cent = nx.center(G)
			print("Center - ",cent)
			diam = nx.diameter(G)
			print("Diameter - ",diam)
			rad = nx.radius(G)
			print("Radius - ",rad)

	print("Draw Graph?")
	key3 = input("y/n? ")
	if (key3 == "y"):
		nx.draw(G, with_labels = True)
		plt.savefig("plot.png")
		plt.show()
	print(nx.info(G))

	#Поменять количество вершин в графе?
	print("Do u want another quantity of Vertex? ")
	key = input("y/n? \n")
	if (key == "y"):
		launch = True
	else: 
		launch = False

import networkx as nx
import time
import pylab as plt
import os

flag = 0
while (flag == 0):
	n = int(input("Enter quantity of Vertex: "))
	p = float(input("Enter probabiluty of edge: "))

	#Генерируем рандомный граф
	G = nx.fast_gnp_random_graph(n,p)
	print(G)
	f = open('time.txt', 'w')
	#Выполняем поиск в ширину и считаем время, за которое он производится
	root = 0
	time.perf_counter()
	edges = nx.bfs_edges(G,root)
	nodes = [root] + [v for u, v in edges]
	times = time.process_time()
	print("BFS time is: ",time.process_time()," seconds")
	f.write(str(times))
	f.close()
	
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

	nonE = nx.non_edges(G)
	print(nonE)
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
	start = 0 #int(input("Enter start vertex: "))
	end = int(input("Enter target: "))
	p = nx.shortest_path(G,source = 0, target = end)
	print(p)
	
	#np = nx.bidirectional_shortest_path(G,start,end)
	#print(np)
	f = open('degree.txt', 'w')
	text1 = 'Degree '
	text2 = ' vertex is '
	tmp = 0
	d = [] * n
	for i in range(n):
	#	print("Degree",i,"vertex is",G.degree[i])
		out = text1 + str(i) + text2 + str(G.degree[i]) + '\n'
		f.write(out)
		d.append(G.degree[i])
	f.close()
	print("To open file with vertex's degrees?")
	keyd = input("y/n? ")
	if (keyd == "y"):
		os.system('degree.txt')
	d = sorted(d)
	print("Max degree - ",max(d))

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
		##d = sorted(d)
	#print(max(d), " - eccentricity")
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
		flag = 0
	else: 
		flag = 1

	
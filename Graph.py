import networkx as nx
import time
import pylab as plt

flag = 0
while (flag == 0):
	n = int(input("Enter quantity of Vertex: "))
	p = float(input("Enter probabiluty of edge: "))

	#Генерируем рандомный граф
	G = nx.fast_gnp_random_graph(n,p)

	f = open('time.txt', 'w')
	#Выполняем поиск в ширину и считаем время, за которое он производится
	root = 0
	time.perf_counter()
	edges = nx.bfs_edges(G,root)
	nodes = [root] + [v for u, v in edges]
	times = time.process_time()
	print(time.process_time()," seconds")
	f.write(str(times))
	f.close()
	
	#Вывести путь поиска в ширину?
	print("Do you want to see BFS way?")
	key1 = input("y/n? \n")
	if (key1 == "y"):
		print(nodes)
	
	if (n <=15):
		nx.draw(G, with_labels = True)
		plt.savefig("plot.png")
		plt.show()
	print("==========================================")
	#Кратчайшие пути: от введенной вершины до всех остальных и от нулевой до введённой
	start = 0 #int(input("Enter start vertex: "))
	end = int(input("Enter target: "))
	p = nx.shortest_path(G,end)
	print(p)
	
	np = nx.bidirectional_shortest_path(G,start,end)
	print(np)

	tmp = 0
	d = [] * n
	for i in range(n):
		print("Degree",i,"vertex is",G.degree[i])
		d.append(G.degree[i])
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
	
	#Поменять количество вершин в графе?
	print("Do u want another quantity of Vertex? ")
	key = input("y/n? \n")
	if (key == "y"):
		flag = 0
	else: 
		flag = 1

	
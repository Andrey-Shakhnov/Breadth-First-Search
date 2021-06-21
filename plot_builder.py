import matplotlib.pyplot as plot


data_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
data_t1 = [3.7, 3.0, 3.0, 2.1, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
data_t2 = [3.4, 2.7, 2.5, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
data_t3 = [2.4, 2.3, 2.3, 2.2, 2.1, 2.1, 2.1, 2.0, 2.0, 2.0, 1.8, 1.8, 1.8, 1.4, 1.3, 1.0, 1.0]
data_t4 = [2.1, 2.0, 2.0, 1.8, 1.5, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

plot.title('Eccentricity value from vertex', fontsize=15)

plot.plot(data_n, data_t1, label='0.2')
plot.plot(data_n, data_t2, label='0.5')
plot.plot(data_n, data_t3, label='0.75')
plot.plot(data_n, data_t4, label='0.9')
plot.grid()
plot.legend()
plot.ylabel('Eccentricity')
plot.xlabel('Vertex')
plot.show()
import random
import matplotlib.pyplot as plt

num_points = 100
x = [random.uniform(0, 50) for i in range(num_points)]
y = [random.uniform(0, 50) for i in range(num_points)]
points = list(zip(x, y))
k = random.randint(3,5)
x1 = [random.uniform(0, 50) for i in range(k)]
y1 = [random.uniform(0, 50) for i in range(k)]
center = list(zip(x1, y1))
plt.scatter(x, y, color='pink', marker='o', label='точки')
plt.scatter(x1, y1, color='green', marker='o', label='центр кластера')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('точки и центры кластеров(первый график)')
plt.show()

def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def cluster_distribution(points, centers): #распределяем точки по кластерам
    clusters = [[] for i in range(len(centers))] #создаём пустые списки для каждого кластера
    for point in points:
        distances = [distance(point, center) for center in centers] #создаем список с расстояниями от точки до центров
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    return clusters

def new_centers(clusters): #вычисляем новые центры
    new_centroids = []
    for cluster in clusters:
        if cluster: #если кластер пустой, то переходим в else
            x_coords, y_coords = zip(*cluster)
            new_centroids.append([sum(x_coords) / len(cluster), sum(y_coords) / len(cluster)])
        else:
            new_centroids.append(random.choice(points)) #присваиваем рандомное значение центру, у которого нет точек
    return new_centroids

def k_means(points, centers, max_iters=100, inaccuracy=0.001):
    global number_of_iterations
    for i in range(max_iters):
        clusters = cluster_distribution(points, centers)
        new_center = new_centers(clusters)
        number_of_iterations += 1
        if all(distance(c, nc) < inaccuracy for c, nc in zip(centers, new_center)): #если расстояние между центрами меньше микро числа, то завершаем все
            break
        centers = new_center
    print("количество итераций =", number_of_iterations)
    return centers, clusters

final_centers, clusters = k_means(points, center)

colors = ['r', 'g', 'b', 'y', 'm']
for cluster_number, cluster in enumerate(clusters):
    if cluster:
        x_c, y_c = zip(*cluster)
        plt.scatter(x_c, y_c, color=colors[cluster_number % len(colors)])
x_final, y_final = zip(*final_centers)
plt.scatter(x_final, y_final, color='black', marker='x', s=100, label='новые центры кластеров')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('результат кластеризации (второй график)')
plt.show()

import random
import matplotlib.pyplot as plt

num_points = 50
x1 = [random.uniform(0, 5) for i in range(num_points)]
y1 = [random.uniform(0, 10) for i in range(num_points)]
class1 = list(zip(x1, y1))
labels1 = [0] * num_points

x2 = [random.uniform(5, 10) for i in range(num_points)]
y2 = [random.uniform(0, 10) for i in range(num_points)]
class2 = list(zip(x2, y2))
labels2 = [1] * num_points

test_x = [random.uniform(0, 10) for i in range(10)]
test_y = [random.uniform(0, 10) for i in range(10)]
test_points = list(zip(test_x, test_y))


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def knn(train_points, train_labels, test_point, k=5):
    distances = []
    for i in range(len(train_points)):
        dist = distance(test_point, train_points[i])
        distances.append((dist, train_labels[i]))
    distances.sort(key=lambda x: x[0])  #сортируем по возрастанию
    k_near = distances[:k]

    votes = {}
    for d, label in k_near:
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1
    return max(votes, key=votes.get)


train_points = class1 + class2
train_labels = labels1 + labels2
predicted_labels = [knn(train_points, train_labels, point, k=5) for point in test_points]

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
x1_c, y1_c = zip(*class1)
x2_c, y2_c = zip(*class2)
plt.scatter(x1_c, y1_c, color='pink', label='класс 1')
plt.scatter(x2_c, y2_c, color='green', label='класс 2')
plt.scatter(test_x, test_y, color='blue', marker='x', s=100, label='тестовые точки')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.title('точки до классификации')

plt.subplot(1, 2, 2)
plt.scatter(x1_c, y1_c, color='pink', label='класс 1')
plt.scatter(x2_c, y2_c, color='green', label='класс 2')
for i, point in enumerate(test_points):
    color = 'pink' if predicted_labels[i] == 0 else 'green'
    plt.scatter(point[0], point[1], color=color, marker='x', s=100)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.title('точки после KNN (при k=5)')

plt.tight_layout()
plt.show()
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x_train = np.array([[1, 1], [2, 2.5], [3, 1.2], [5.5, 6.3], [6, 9], [7, 6]])
y_train = ['red', 'red', 'red', 'blue', 'blue', 'blue']

x_test = np.array([3, 4])

# plt.figure()
# plt.scatter(x_train[:, 0], x_train[:, 1], s=170, color=y_train[:])
# plt.scatter(x_test[0], x_test[1], s=170, color='green')
# plt.show()


def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


num = len(x_train)
distance = np.zeros(num)
for i in range(num):
    x = x_train[i]
    distance[i] = dist(x, x_test)
minim = np.argmin(distance)

print(y_train[minim])



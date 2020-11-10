# 4 Backend 36 Worker

import matplotlib.pyplot as plt
import numpy as np


f = open("./data/4-36/200.csv", "r")
csv200 = f.readlines()
csv200.pop(0)
data200 = []
iteration = []
f.close()

for i, l in enumerate(csv200):
    iteration.append(i)
    data200.append(int(l.split(",")[1]))


f = open("./data/4-36/500.csv", "r")
csv500 = f.readlines()
csv500.pop(0)
data500 = []
f.close()

for l in csv500:
    data500.append(int(l.split(",")[1]))


plt.plot(iteration, data200, label='200 Devices')
plt.plot(iteration, data500, label='500 Devices')

plt.xlabel('Iteration')
plt.ylabel('Response Time (Milliseconds)')
plt.legend()
plt.show()

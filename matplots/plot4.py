# 200 Devs

import matplotlib.pyplot as plt
import numpy as np


f = open("./data/4-4/200.csv", "r")
csv4 = f.readlines()
csv4.pop(0)
data4 = []
iteration = []
f.close()

for i, l in enumerate(csv4):
    iteration.append(i)
    data4.append(int(l.split(",")[1]))


f = open("./data/4-12/200.csv", "r")
csv12 = f.readlines()
csv12.pop(0)
data12 = []
f.close()

for l in csv12:
    data12.append(int(l.split(",")[1]))


f = open("./data/4-36/200.csv", "r")
csv36 = f.readlines()
csv36.pop(0)
data36 = []
f.close()

for l in csv36:
    data36.append(int(l.split(",")[1]))


plt.plot(iteration, data4, label='4 Workers')
plt.plot(iteration, data12, label='12 Workers')
plt.plot(iteration, data36, label='36 Workers')

plt.xlabel('Iteration')
plt.ylabel('Response Time (Milliseconds)')
plt.legend()
plt.show()

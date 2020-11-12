# 200 Devs

import matplotlib.pyplot as plt
import numpy as np


f = open("./data/6-26/300.csv", "r")
csv4 = f.readlines()
csv4.pop(0)
data4 = []
iteration = []
f.close()

for i, l in enumerate(csv4):
    iteration.append(i)
    data4.append(int(l.split(",")[1]))


f = open("./data/6-26-2R/300.csv", "r")
csv12 = f.readlines()
csv12.pop(0)
data12 = []
f.close()

for l in csv12:
    data12.append(int(l.split(",")[1]))


f = open("./data/6-24-2R/300.csv", "r")
csv36 = f.readlines()
csv36.pop(0)
data36 = []
f.close()

for l in csv36:
    data36.append(int(l.split(",")[1]))


plt.plot(iteration, data4, label='2 Free Threads 1 Job Queue')
plt.plot(iteration, data12, label='2 Free Threads 2 Job Queue')
plt.plot(iteration, data36, label='4 Free Threads 2 Job Queue')

plt.xlabel('Iteration')
plt.ylabel('Response Time (Milliseconds)')
plt.legend()
plt.show()

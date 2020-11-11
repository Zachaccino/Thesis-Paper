# 4 Backend 4 Worker

import matplotlib.pyplot as plt
import numpy as np


f = open("./data/4-4/50.csv", "r")
csv50 = f.readlines()
csv50.pop(0)
data50 = []
iteration = []
f.close()

for i, l in enumerate(csv50):
    iteration.append(i)
    data50.append(int(l.split(",")[1]))

print("AVG 50 Devs: ", round(sum(data50)/len(data50),2))

f = open("./data/4-4/100.csv", "r")
csv100 = f.readlines()
csv100.pop(0)
data100 = []
f.close()

for l in csv100:
    data100.append(int(l.split(",")[1]))

print("AVG: 100 Devs", round(sum(data100)/len(data100),2))

f = open("./data/4-4/200.csv", "r")
csv200 = f.readlines()
csv200.pop(0)
data200 = []
f.close()

for l in csv200:
    data200.append(int(l.split(",")[1]))

print("AVG: 200 Devs", round(sum(data200)/len(data200),2))

plt.plot(iteration, data50, label='50 Devices')
plt.plot(iteration, data100, label='100 Devices')
plt.plot(iteration, data200, label='200 Devices')

plt.xlabel('Iteration')
plt.ylabel('Response Time (Milliseconds)')
plt.legend()
plt.show()

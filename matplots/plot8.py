# 1000

import matplotlib.pyplot as plt
import numpy as np


f = open("./data/8-6/1000.csv", "r")
csv4 = f.readlines()
csv4.pop(0)
data4 = []
iteration = []
f.close()

for i, l in enumerate(csv4):
    iteration.append(i)
    data4.append(int(l.split(",")[1]))


plt.plot(iteration, data4, label='6 Backends 8 Workers')

plt.xlabel('Iteration')
plt.ylabel('Response Time (Milliseconds)')
plt.legend()
plt.show()

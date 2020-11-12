# 4-4 Avg Respon

import matplotlib.pyplot as plt
import numpy as np

dev_count = [50, 100, 200]
resp = [4.03, 4.87, 5.26]

plt.plot(dev_count, resp)
plt.xlabel('Number of Simulated Devices')
plt.ylabel('Average Response Time (Milliseconds)')


for a,b in zip(dev_count, resp): 
    plt.text(a, b, str(b))

plt.show()

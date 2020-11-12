# 4-4 Avg Delay

import matplotlib.pyplot as plt
import numpy as np

dev_count = [50, 100, 200]
resp = [0, 4, 16]

plt.plot(dev_count, resp)
plt.xlabel('Number of Simulated Devices')
plt.ylabel('Delay(Minutes)')


for a,b in zip(dev_count, resp): 
    plt.text(a, b, str(b))

plt.show()

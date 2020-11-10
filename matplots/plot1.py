# 4 Backend 4 Worker

import matplotlib.pyplot as plt
import numpy as np

N = 50
x1 = np.random.rand(N)
y1 = np.random.rand(N)
x2 = np.random.rand(N)
y2 = np.random.rand(N)

plt.plot(x1, y1, label='4-4')
plt.title('Response time for each iteration')
plt.xlabel('Iteration')
plt.ylabel('Response Time (Milliseconds)')
plt.legend()
plt.show()

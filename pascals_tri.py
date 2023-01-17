import numpy as np
import math
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import time


def ariana_pascal(n):
    for row in range(n):
        line= np.array([])
        for num in range(row+1):
            x=  math.factorial(row)/(math.factorial(num)* math.factorial(row-num))
            line= np.append(line, x)
        print(line)


times = []
n_iters = 200
for i in range(n_iters):
    start = time.time()
    ariana_pascal(i+1)
    end = time.time()
    times.append(end - start)

plt.scatter(x=range(n_iters), y=times)
plt.xlabel("number of lines")
plt.ylabel("time to print")
plt.savefig("pascal_time.png")

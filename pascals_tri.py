import numpy as np
import math

n= 15
for row in range(n):
    line= np.array([])
    for num in range(row+1):
        x=  math.factorial(row)/(math.factorial(num)* math.factorial(row-num))
        line= np.append(line, x)
    print(line)

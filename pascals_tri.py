import numpy as np
import math

def pascal(n):
    for row in range(n):
        line= np.array([])
        for num in range(row+1):
            x=  math.factorial(row)/(math.factorial(num)* math.factorial(row-num))
            line= np.append(line, x)
        print(line)

if __name__ == '__main__':
    pascal(10)
    
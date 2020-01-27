import numpy as np



N,M = map(int,input().split())
a = np.array([input().split() for _ in range(N)], int)
b = np.array([input().split() for _ in range(N)], int)
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n'

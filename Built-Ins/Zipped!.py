import numpy as np

x,n = map(int,input().split())

arr = []

for i in range(n):
    arr.append(list(map(float,input().split())))

[print(sum(a)/len(a)) for a in zip(*arr)]


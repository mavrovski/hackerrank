import math
from math import sqrt

ab = float(input())
bc = float(input())

h = sqrt(pow(ab,2)+pow(bc,2))

h = h/2.0
adj = bc/2.0
result = int(round(math.degrees(math.acos(adj/h))))
print("{0}°".format(result))
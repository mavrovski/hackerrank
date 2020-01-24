import numpy as np

np.set_printoptions(sign=' ')
my_arr = np.array(list(map(float, input().split())))
print(np.floor(my_arr))
print(np.ceil(my_arr))
print(np.rint(my_arr))

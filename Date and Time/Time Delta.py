import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, fmt)
    t2 = datetime.strptime(t2, fmt)
    return str(int(abs((t2 - t1).total_seconds())))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
        # fptr.write(delta + '\n')

    # fptr.close()



# 2 way

# import datetime
#
# def read_datetime():
#     return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
#
# def main():
#     T = int(input())
#     for _ in range(T):
#         t1 = read_datetime()
#         t2 = read_datetime()
#
#
#         print(int(abs(t1 - t2).total_seconds()))
# if __name__ == '__main__':
#     main()

import re

t = int(input())


for i in range(t):
    regex_str = input()
    answer=True
    try:
        re.compile(regex_str)
    except re.error:
        answer = False
    print(answer)

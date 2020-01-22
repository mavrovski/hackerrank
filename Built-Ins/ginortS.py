import numpy as np

word = input()

l=[x for x in sorted(word) if x.islower()]
u = [x for x in sorted(word) if x.isupper()]
d = [x for x in sorted(word) if x.isdigit()]
odds = [x for x in map(int,d) if x%2==1]+[x for x in map(int,d) if x%2==0]
res = list(map(str,(l+u+odds)))

print(''.join(res))

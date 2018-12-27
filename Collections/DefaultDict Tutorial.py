from collections import defaultdict

defdict, n = defaultdict(list), list(map(int, input().split()))

for i in range(n[0]):
    defdict[input()].append(i + 1)

for i in range(n[1]):
    print(' '.join(map(str, defdict[input()])) or -1)
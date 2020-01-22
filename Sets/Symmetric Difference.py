
n = int(input())
set_one = set(map(int,input().split()))
m = int(input())
set_two = set(map(int,input().split()))

diff_set_one = set_one.difference(set_two)
diff_set_two = set_two.difference(set_one)
result = sorted(diff_set_one.union(diff_set_two))

print(*result,sep="\n")
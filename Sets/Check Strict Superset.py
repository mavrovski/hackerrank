input_set  = set(map(int,input().split()))
n = int(input())
output_set = set()
for i in range(n):
    output_set.update(map(int,input().split()))

# print(output_set)
print(input_set == input_set.union(output_set))



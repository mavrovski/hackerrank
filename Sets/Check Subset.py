total_sets = int(input())

for i in range(0,total_sets):
    input();set_A = set(map(int,input().split()))
    input();set_B = set(map(int, input().split()))
    print(set_B==set_A.union(set_B))




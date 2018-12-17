from itertools import permutations


values = list(input().split())
word = values[0]
count = int(values[1])

permutations_result = (list(permutations(word,count)))

result = [list(t) for t in permutations_result]


result_two = sorted(result)

for i in range(0,len(result_two)):
    print(*result_two[i],sep='')

def fibonacci_recur(n):
    if n <=1:
        return n
    else:
        return (fibonacci_recur(n-1)+fibonacci_recur(n-2))


number = int(input())
result = []
for i in range(0,number):
    result.append(fibonacci_recur(i))

result3 = list((map(lambda x:x**3,(result))))
print(result3)


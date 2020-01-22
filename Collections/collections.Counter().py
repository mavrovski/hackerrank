from collections import Counter


number_of_shoes = int(input())
list_of_shoes=list(map(int,input().split()))
number_of_customers=int(input())


total_sum = 0
for i in range(1,number_of_customers+1):
    n = list(map(int,input().split()))
    customer_number = n[0]
    price = n[1]
    for j in list_of_shoes:
        if(j==customer_number):
            total_sum=total_sum+price
            list_of_shoes.remove(customer_number)
            break

print(total_sum)
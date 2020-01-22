number_of_tests = int(input())

for i in range(number_of_tests):
    args = input().split()

    try:
        divisible = int(args[0])
        divisor = int(args[1])
        print("{0}".format(divisible//divisor))
    except BaseException as e:
        print("Error Code:",e)



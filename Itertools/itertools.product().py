from itertools import product


def product_result(A,B):
    return (list(product(A,B)))



if __name__ == '__main__':
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))


    result = product_result(A,B)
    print(*result,sep=' ')



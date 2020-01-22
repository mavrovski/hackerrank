def numbers_to_n(n):
    numbers = list(range(1,n+1))
    print(*numbers,sep='')

if __name__ == '__main__':
    n = int(input())
    numbers_to_n(n)

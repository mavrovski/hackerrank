def average(array):
    set_arr = set(array)
    result = sum(set_arr)/len(set_arr)
    return result
    # your code goes here


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
import re

def detect_fp_number(s):
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'
    res = bool(re.match(pattern,s))
    # res = [i for i in s if re.match(pattern,s)]
    return  res


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(detect_fp_number(input()))
import re

def fun(s):
    pattern = r"^[\w-]{1,}@{1}[a-zA-Z0-9]{1,}\.[a-zA-Z0-9]{1,3}$"
    l = [i for i in s if re.match(pattern, s)]
    return l


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
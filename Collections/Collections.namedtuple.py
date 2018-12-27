from collections import namedtuple
n = int(input())
columns = ','.join(input().split())
Student = namedtuple('Student',columns)
summed = 0

for i in range(n):
    line = input().split()
    student = Student(*line)
    summed += float(student.MARKS)


print(summed/n)

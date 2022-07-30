import sys

n = int(sys.stdin.readline())
students = []

for i in range(n):
    age, name = map(str,sys.stdin.readline().split())
    age = int(age)
    students.append([age,name])

students.sort(key = lambda x : x[0])

for i in students:
    print(i[0],i[1])
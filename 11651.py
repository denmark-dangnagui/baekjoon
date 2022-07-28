import sys
n = int(input())
numbers = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    numbers.append(a)

numbers.sort(key = lambda x : x[1])
for i in range(n):
    for j in range(2):
        print(numbers[i][j],end=' ')
    print()
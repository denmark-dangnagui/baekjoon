import sys

n = int(input())

numbers = list(map(int,sys.stdin.readline().split()))

numbers1 = list(sorted(set(numbers)))

dic = {numbers1[i] : i for i in range(len(numbers1))}
for i in numbers:
    print(dic[i], end =' ')
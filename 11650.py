import sys
n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    nums = list(map(int,sys.stdin.readline().split()))
    numbers.append(nums)

numbers.sort(key = lambda x:-x[0])
for i in range(n):
    for j in range(2):
        print(numbers[i][j],end = ' ')
    print()
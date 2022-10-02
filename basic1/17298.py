import sys
from collections import deque
n = int(input())
numbers = deque(list(sys.stdin.readline().split()))
stack = [-1] * n
temp = [0]
for i in range(1,n):
    while temp and numbers[temp[-1]] < numbers[i]:
        stack[temp.pop()] = numbers[i]
    temp.append(i)
print(*stack)

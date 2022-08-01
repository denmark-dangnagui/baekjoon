import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().split()
    for j in s:
        print(j[::-1],end=' ')
    print()
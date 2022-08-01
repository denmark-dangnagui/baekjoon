import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().split()
    for j in s:
        j = list(j)
        j.reverse()
        a = ''.join(j)
        print(a, end='')
        print(end=' ')
    print()
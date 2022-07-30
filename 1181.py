import sys
n = int(input())
l = []
for i in range(n):
    temp = sys.stdin.readline().strip()
    l.append(temp)
l = list(set(l))
l.sort()
l.sort(key = len)
for i in l:
    print(i)

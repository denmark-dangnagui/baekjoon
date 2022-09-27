import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
queue = deque()
queue2 = deque()
for i in range(1, n + 1):
    queue.append(i)
cnt = 0
while queue:
    cnt += 1
    queue.append(queue.popleft())
    if cnt == k:
        queue2.append(queue.pop())
        cnt = 0
queue2 = map(str,queue2)
print("<", ", ".join(queue2)[:], ">",sep='')
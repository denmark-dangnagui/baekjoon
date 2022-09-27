from collections import deque
import sys
queue = deque()
size = 0
n = int(input())

for i in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        queue.appendleft(order[1])
        size += 1
    elif order[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(queue.pop())
            size -= 1
    elif order[0] == 'size':
        print(size)
    elif order[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(queue[-1])
    elif order[0] == 'back':
        if size == 0:
            print(-1)
        else:
            print(queue[0])
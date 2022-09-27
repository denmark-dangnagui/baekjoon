import sys
from collections import deque
queue = deque()
size = 0
n = int(sys.stdin.readline())

for i in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        queue.appendleft(order[1])
        size += 1
    elif order[0] == 'push_back':
        queue.append(order[1])
        size += 1
    elif order[0] == 'pop_front':
        if size != 0:
            print(queue.popleft())
            size -= 1
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if size != 0:
            print(queue.pop())
            size -= 1
        else:
            print(-1)
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
            print(queue[0])
    elif order[0] == 'back':
        if size == 0:
            print(-1)
        else:
            print(queue[-1])
import sys
from collections import deque
queue1 = deque(sys.stdin.readline())
queue2 = deque()
temp = deque()
cnt = 0
queue1.remove('\n')
while queue1:
    if queue1[0] == '<':
        while queue1[0] != '>':
            queue2.append(queue1.popleft())
        queue2.append(queue1.popleft())
    else:
        temp.append(queue1.popleft())
        if queue1 and queue1[0] == '<':
            while temp:
                queue2.append(temp.pop())
        if queue1 and queue1[0] == ' ':
            while temp:
                queue2.append(temp.pop())
            queue2.append(queue1.popleft())
if temp:
    while temp:
        queue2.append(temp.pop())
for i in queue2:
    print(i,end='')
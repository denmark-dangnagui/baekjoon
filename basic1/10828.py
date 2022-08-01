import sys
n = int(sys.stdin.readline())
stack = []
size = 0

for i in range(n):
    order = sys.stdin.readline().split() # 이거 정리해둬 나중에 유용할거야
    if order[0] == 'push':
        stack.append(order[1])
        size += 1
    elif order[0] == 'pop':
        if size > 0:
            print(stack[-1])
            stack.pop()
            size -= 1
        else:
            print(-1)
    elif order[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if size > 0:
            print(stack[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(size)
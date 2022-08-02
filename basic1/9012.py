import sys

n = int(sys.stdin.readline())

for k in range(n):
    s = sys.stdin.readline()
    size = 0
    stack = []
    temp = []
    for i in range(len(s) - 1):
        stack.append(s[i])
    for i in range(len(s) - 1):
        if stack[-1] == ')':
            temp.append(stack[-1])
            stack.pop()
        elif stack[-1] == '(':
            if len(temp) == 0:
                temp.append(stack[-1])
            elif temp[-1] == ')':
                temp.pop()
                stack.pop()
            else:
                temp.append(stack[-1])
                stack.pop()
    if len(temp) != 0:
        print('NO')
    else:
        print('YES')
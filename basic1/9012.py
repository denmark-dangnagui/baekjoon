import sys

stack1 = []
stack2 = []
size1 = 0
n = int(sys.stdin.readline())

for i in range(n):
    g = sys.stdin.readline()
    for j in g:
        stack1.append(j)
    stack1.remove('\n')
    for j in range(len(stack1)):
        temp = stack1.pop()
        if len(stack2) == 0:
            if temp == '(':
                stack2.append(temp)
                break
            else:
                stack2.append(temp)
        else:
            if temp == '(':
                if stack2[-1] == ')':
                    stack2.pop()
                else:
                    stack2.append(temp)
            else:
                stack2.append(temp)
    if len(stack2) == 0:
        print('YES')
    else:
        print('NO')
    stack2.clear()
    stack1.clear()
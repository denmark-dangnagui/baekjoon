import sys
stack = []
stick = list(sys.stdin.readline())
stick.remove('\n')
answer = 0
temp = 0
for i in stick[::-1]:
    if temp == '(':
        if i == '(':
            stack.pop()
            answer += 1
        else:
            stack.append(stick.pop())
        temp = i
    else:
        if i == ')':
            stack.append(stick.pop())
        if i == '(':
            stack.pop()
            answer += len(stack)
        temp = i
print(answer)
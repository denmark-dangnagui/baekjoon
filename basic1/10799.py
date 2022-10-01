import sys
stack = []
stick = list(sys.stdin.readline())
stick.remove('\n')
answer = 0
cnt = 0
for i in stick[::-1]:
    if i == ')':
        stack.append(stick.pop())
    if i == '(':
        stack.pop()
        answer += len(stack)

    temp = i
# print(stick)
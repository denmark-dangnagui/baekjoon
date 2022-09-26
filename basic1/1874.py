import sys
n = int(sys.stdin.readline())
j = 0
answer = []
stack1 = []
stack2 = []
stack3 = []
for i in range(n):
    stack1.append(int(sys.stdin.readline()))
for i in range(1,n + 1):
    cnt = 0
    stack2.append(i)
    answer.append('+')
    while stack2 and stack1[j] == stack2[-1]:
        stack3.append(stack2.pop())
        j += 1
        cnt += 1
        answer.append('-')
if stack1 == stack3:
    for i in answer:
        print(i)
else:
    print('NO')
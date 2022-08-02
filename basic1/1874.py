import sys
n = int(sys.stdin.readline())
temp = []
stack1 = []
stack2 = []
stack3 = []
for i in range(n):
    temp.append(int(sys.stdin.readline()))
max_num = 0
for j in temp:
    if j > max_num:
        for i in range(max_num + 1,j + 1):
            stack1.append(i)
            stack2.append('+')
        max_num = j
        stack2.append('-')
        stack3.append(stack1.pop())
    else:
        stack3.append(stack1.pop())
        stack2.append('-')
if temp == stack3:
    for i in stack2:
        print(i)
else:
    print("NO")
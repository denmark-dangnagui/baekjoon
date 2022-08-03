import sys

l = []
s = sys.stdin.readline()
for i in s:
    if i != '\n':
        l.append(i)
n = int(sys.stdin.readline())
s_len = len(l)
for i in range(n):
    o = sys.stdin.readline().split()
    if o[0] == 'P':
        # print('len',s_len)
        l.insert(s_len, o[1])
        s_len += 1
        # print(l)
    elif o[0] == 'L':
        # print(s_len)
        if s_len > 0:
            s_len -= 1
            # print(1)
        else:
            s_len = 0
            # print(2)
    elif o[0] == 'D':
        # print('len',s_len)
        if s_len != len(s):
            s_len += 1
        else:
            s_len =len(s)
    elif o[0] == 'B':
        # print('len',s_len)
        if s_len != 0:
            del l[s_len-1]
            if s_len != 0:
                s_len -= 1
        # print(l)
for i in l:
    print(i,end='')
import sys

word = list(sys.stdin.readline())
n = int(sys.stdin.readline())
cursor = len(word)-1
for i in range(n):
    order = list(sys.stdin.readline())
    if order[0] == 'P':
        word.insert(cursor,order[2])
        cursor += 1
    elif order[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif order[0] == 'D':
        if cursor != len(word) - 1:
            cursor += 1
    elif order[0] == 'B':
        if cursor != 0:
            del word[cursor - 1]
            cursor -= 1
print(''.join(word))
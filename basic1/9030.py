import sys

n = int(sys.stdin.readline())
for i in range(n):
    sentence = sys.stdin.readline().split()
    print(sentence)
    for j in sentence:
        print(j[::-1],end=' ')
    print()


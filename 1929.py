m, n = map(int, input().split())
num_list = []
for i in range(m,n+1):
    cnt = 0
    for j in range(2,int(i**0.5) + 1):
        if i % j == 0:
           cnt += 1
    if cnt == 0:
        print(i)

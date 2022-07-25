n,m = map(int,input().split())

a = list(map(int,input().split()))
b = []
c = []
total = 0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            total = a[i] + a[j] + a[k]
            b.append(total)

for i in b:
    if i <= m:
        c.append(i)

print(max(c))
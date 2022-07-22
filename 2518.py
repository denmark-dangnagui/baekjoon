a = int(input())
b = int(input())

prime = []

for i in range(a,b+1):
    cnt = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            prime.append(i)

if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
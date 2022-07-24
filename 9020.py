def isPrime(n):
    a = [True] * (n + 1)
    m = int(n ** 0.5)
    b = []
    for i in range(2, m + 1):
        for j in range(i + i, n + 1, i):
            a[j] = False
    for i in range(2,n+1):
        if a[i]:
            b.append(i)
    return b

t = int(input())
b = []
for i in range(t):
    cha = 10000
    a1 = 0
    a2 = 0
    n = int(input())
    b = isPrime(n)
    for j in b:
        for k in b:
            if j + k == n:
                t1 = j
                t2 = k
                temp = abs(t1 - t2)
                if temp < cha:
                    a1 = t1
                    a2 = t2
                    cha = temp
    print(a1,a2)

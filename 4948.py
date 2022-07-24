def isPrime(n2,n):
    a = [True] * (n2 + 1)
    m = int(n2**0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n2 + 1, i):
                a[j] = False
    print(len([i for i in range(n+1, n2) if a[i] == True]))

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        n2 = n * 2
        isPrime(n2,n) 
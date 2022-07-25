i = int(input())
b = []
for n in range(i):
    temp = n
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    total += temp
    if total == i:
        b.append(temp)
if len(b) ==0:
    print(0)
else:
    print(min(b))
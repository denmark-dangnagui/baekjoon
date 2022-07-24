a = int(input())
if a == 0:
    print(1)
else:
    total = 1
    for i in range(1,a+1):
        total *= i
    print(total)

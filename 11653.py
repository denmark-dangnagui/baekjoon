num = int(input())

while 1:
    for i in range(2,num+1):
        if num % i == 0:
            print(i)
            num = num // i
            break
    if num == 1:
        break
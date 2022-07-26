n = int(input())
cnt = 0
num = 666
while True:
    temp = num
    e = 0
    while 1:
        t = temp % 10
        if t == 6:
            e += 1
        else:
            e = 0
        if e == 3:
            cnt += 1
            break
        elif temp == 0:
            break
        temp = temp // 10
    if cnt == n:
        print(num)
        break
    num += 1
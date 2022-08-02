n = int(input())

temp = 2
cycle = 1

while n > cycle:
    cycle += temp
    temp += 1

temp -= 1
i = cycle - temp + 1
i2 = n - i

if temp % 2 != 0:
    m = temp
    s = 1
    if i2 != 0:
        for i in range(i2):
            m -= 1
            s += 1
        print(str(m) + '/' + str(s))
    else:
        print(str(m) + '/' + str(s))

else:
    m = 1
    s = temp
    if i2 != 0:
        for i in range(i2):
            m += 1
            s -= 1
        print(str(m) + '/' + str(s))
    else:
        print(str(m) + '/' + str(s))
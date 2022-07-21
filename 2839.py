n = int(input())
#3킬로 5킬로
cnt5 = 0
cnt3 = 0
while n > 0:
    if n % 5 == 0:
        cnt5 = n // 5
        break
    else:
        n -= 3
        cnt3 += 1

if n < 0:
    print(-1)
else:
    cnt = cnt3 + cnt5
    print(cnt)
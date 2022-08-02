a = int(input())

temp = 1    # 임의의 수
cnt = 1     # 몇번째 줄에 있는지
n = 6       # 더해줄 수
if a == 1:  # 만일 1이라면
    print(1)
else:
    while temp < a:     # temp를 통해 제어하여 몇번째 줄에 있는지 확인
        temp += n       # 6의 배수만큼 각 줄에 있는 최대 수가 커지므로
        n += 6          # 6의 배수를 만들기 위해
        cnt += 1        # 몇번째 줄인지 알기 위해
    print(cnt)
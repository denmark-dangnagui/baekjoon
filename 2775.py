t = int(input())

for i in range(t):
    floor = int(input())
    ho = int(input())
    cnt = [i+1 for i in range(ho)]

    for j in range(floor):
        for k in range(1,ho):
            cnt[k] += cnt[k-1]
    print(cnt[-1])

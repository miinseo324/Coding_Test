n, k = map(int, input().split()) # n: 식탁의 길이, k: 햄버거 먹을 수 있는 거리
hbg = list(input())

max_p = 0

for i in range(n):
    if hbg[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if hbg[j] == 'H':
                hbg[j] = 0
                max_p += 1
                break

print(max_p)
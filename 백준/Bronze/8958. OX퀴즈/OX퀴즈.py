x = int(input())
for i in range(x):
    sum, cnt = 0, 0
    ox = input()
    for i in ox:
        if i == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
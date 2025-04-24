a, b = map(int, input().split())
cnt = 1

while (a!=b):
    if a > b:
        cnt = -1
        break
    else:
        if b%10 == 1:
            b = (b-1)//10
            cnt += 1
        elif b%2 == 0:
            b = b/2
            cnt += 1
        else:
            cnt = -1
            break

print(cnt)
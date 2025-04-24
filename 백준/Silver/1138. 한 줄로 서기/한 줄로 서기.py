n = int(input())
data = list(map(int, input().split()))
lst = [0]*n
cnt = 1
for i in data:
    x = i
    if lst[i] == 0 and len([y for y in lst[:x] if y>cnt or y == 0]) == i:
        lst[i] = cnt
    else:
        while True:
            x += 1
            if lst[x] == 0 and len([y for y in lst[:x] if y>cnt or y == 0]) == i:
                lst[x] = cnt
                break
    cnt += 1

print(' '.join(map(str, lst)))
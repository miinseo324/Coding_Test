n =int(input()) # 국회의원 수
lst = [0]*n
cnt = 0

for i in range(n):
    lst[i] = int(input()) # 다솜이는 기호 1번

while True:
    if n ==1 or lst[0] > max(lst[1:]):
        break
    else:
        lst[lst[1:].index(max(lst[1:]))+1] -= 1
        lst[0] += 1
        cnt += 1

print(cnt)
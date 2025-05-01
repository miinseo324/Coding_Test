t = int(input()) # 테스트케이스
for i in range(t):
    h, w, n = map(int, input().split())
    yy = n%h
    if yy == 0:
        yy = h
        xx = n//h
    else:
        xx = n//h+1
    if len(str(xx)) == 1:
        print(f'{yy}0{xx}')
    else:
        print(f'{yy}{xx}')
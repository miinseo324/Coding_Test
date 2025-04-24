num = 0
while True:
    L, P, V = map(int, input().split())
    cnt = 0
    if not (1 < L < P < V):
        break;
    elif L == P == V == 0:
        break;
    
    cnt = (V//P)*L
    if V%P > L:
        cnt += L
    else:
        cnt += V%P
    num += 1
    print(f'Case {num}: {cnt}')
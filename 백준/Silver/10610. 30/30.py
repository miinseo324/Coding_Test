# 30의 배수가 되려면, 3의 배수 조건과 10의 배수 조건을 모두 충족해야 한다.
# 3의 배수 조건: 모든 수의 합이 3의 배수이어야 한다. 
# 10의 배수 조건: 맨 마지막이 0이어야 한다.

n = list(map(int, list(input())))
if (sum(n)%3) == 0 and (0 in n):
    print(''.join(map(str, (sorted(n, reverse=True)))))
else:
    print(-1)
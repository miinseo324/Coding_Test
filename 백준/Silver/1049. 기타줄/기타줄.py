n, brand = map(int,input().split()) # n: 끊어진 기타줄 개수, brand: 기타줄 브랜드 종류
pack_p = []
single_p = []

for i in range(brand): # 각 브랜드의 패키지 가격과 낱개 가격 / 패키지는 6개씩
    x,y = map(int, input().split())
    pack_p.append(x)
    single_p.append(y)
    
# 기타줄이 6개 이상일 경우, 무조건 패키지[0]를 사는 것이 이득이다. -> 패키지 중 최솟값 고르기
# 6개 미만일 경우, [1] 중에서 가장 최소값을 골라 곱해라 
sum1, sum2, sum3 = 0, 0, 0

if n//6 != 0:
    sum1 += min(pack_p) * (n//6)

if n%6 != 0:
    sum1 += min(single_p) * (n%6)
    
sum2 = min(pack_p) * (n//6 + 1 if n%6 != 0 else n//6)
sum3 = min(single_p) * n

print(min(sum1, sum2, sum3))    
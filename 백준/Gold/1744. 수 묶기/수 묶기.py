n = int(input())

plus = []
minus = []

result = 0
for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else: # 1일경우 더해주는게 무조건 크다
        result+=num
        
# 정렬 
plus.sort(reverse=True)
minus.sort()

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >=len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)
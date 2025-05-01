ans = 1
for i in range(3):
    ans *= int(input())

for i in '0123456789':
    print(str(ans).count(i))
    
# count 함수는 문자열에서 작동함.
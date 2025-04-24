n = int(input()) # 단어의 개수 n개 주어짐
alpha = {} # 알파벳 딕셔너리 만들자 
voca = [] # 입력 받은 단어 넣을 곳

for i in range(n):
    voca.append(input()[::-1]) # 문자로 입력받는다 -> 리스트 활용할 것임 + 거꾸로 저장
    
for i in voca:
    for j in range(len(i)):
        if i[j] not in alpha: # 만약 이 알파벳이 딕셔너리에 없다면,
            alpha[i[j]] = 10**j
        else:
            alpha[i[j]] += 10**j


sorted_alpha = dict(sorted(alpha.items(), key = lambda x: x[1], reverse=True)) # 내림차순으로 정렬 value 기준

cnt = 9
sum = 0
for y in sorted_alpha.values():
    sum += y * cnt
    cnt -= 1

print(sum)
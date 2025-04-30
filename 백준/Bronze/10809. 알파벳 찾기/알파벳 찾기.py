# 첫째 줄에는 알파벳 소문자로만 이루어진 단어 s가 주어진다.
s = input()
ans = [-1] * 26 # 알파벳의 개수는 26개이므로

for i in range(len(s)):
    if ans[ord(s[i])-97] == -1:
        ans[ord(s[i])-97] = i

print(*ans)
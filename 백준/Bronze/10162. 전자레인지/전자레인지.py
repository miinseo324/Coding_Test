t=int(input()) # 초단위
btn=[300, 60, 10] # a,b,c
total=[]
for i in btn:
  total.append(t//i)
  t=t%i
if t!=0:
  print("-1")
else:
  print(*total)
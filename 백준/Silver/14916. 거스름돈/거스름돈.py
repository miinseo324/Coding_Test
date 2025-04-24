rest = int(input())


coin2, coin5 = 0, rest//5
rest = rest - coin5*5

while (True):
    if rest%2==0:
        coin2 = rest//2
        print(coin2+coin5)
        break
    elif coin5 == 0 and rest%2 != 0:
        print(-1)
        break
    else:
        coin5-=1 
        rest+=5
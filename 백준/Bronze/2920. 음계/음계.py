x = list(map(int,input().split()))
i = 0
if x[0] < x[1]:
    state = 'ascending'
else:
    state = 'descending'
    
while (i < len(x)-2):
    i += 1
    if state == 'ascending':
        if x[i] < x[i+1]:
            continue
        else:
            state = 'mixed'
    elif state == 'descending':
        if x[i] > x[i+1]:
            continue
        else:
            state = 'mixed'
    else:
        break

print(state)
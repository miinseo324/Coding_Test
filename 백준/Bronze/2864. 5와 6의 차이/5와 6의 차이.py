x, y = input().split()

min_x = ['5' if i == '6' else i for i in x]
min_y = ['5' if i == '6' else i for i in y]
max_x = ['6' if i == '5' else i for i in x]
max_y = ['6' if i == '5' else i for i in y]

min_value = int(''.join(min_x)) + int(''.join(min_y))
max_value = int(''.join(max_x)) + int(''.join(max_y))

print(min_value, max_value)
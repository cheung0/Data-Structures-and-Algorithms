n = int (input())

plus_total = 0
minus_total = 0
for i in range(n):
    m = input()
    plus = 0
    minus = 0
    for i in range(len(m)):
        if m[i] == '+':
            plus += 1
        elif m[i] == '-':
            minus += 1
    if plus == 2:
        plus_total += 1
    elif minus == 2:
        minus_total += 1
x = 0
x += plus_total
x -= minus_total
print(x)
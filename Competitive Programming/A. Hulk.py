n = int (input())

res = ''

while n > 1:
    if n % 2 == 1:
        res += 'I love that '
    else:
        res += 'I hate that '
    n -= 1

if n % 2 == 0:
    res += 'I hate it'
else:
    res += 'I love it'

print(res)

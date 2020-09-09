n = int (input())

for i in range(n):
    a, b, c, n = map(int, (input().split()))
    sum = a + b + c + n
    big = max(a, b, c)
    average = big * 3 - a + b + c
    if sum % 3 == 0 and average >= n:
        print('YES')
    else:
        print('NO')


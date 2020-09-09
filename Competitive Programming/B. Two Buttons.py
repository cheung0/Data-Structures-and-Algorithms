n, m = map(int, input().split())

k = 0
while n != m:
    if m % 2 == 0 and m > 0:
        m //= 2
    else:
        m -= 1
    k += 1

print(k)

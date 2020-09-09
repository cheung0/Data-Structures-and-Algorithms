a, b = map(int, input().split())

num = 0

while a <= b:
    a *= 3
    b *= 2
    num += 1
print(num)
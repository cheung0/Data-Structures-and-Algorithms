l = list(map(int, input().split()))
n = l[0]
a = l[1]
b = l[2]
c = l[3]

if a + b + c == n:
    print(3)
elif a + b == n or b + c == n or a + c == n:
    print(2)
elif a == n or b == n or c == n:
    print(1)
else:
    print(0)
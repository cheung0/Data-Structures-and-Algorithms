a = int (input())
b = int (input())
c = int (input())

d = (a + b) * c
e = a * (b + c)
f = a * b * c
g = a + b + c
h = a + (b * c)
i = (a * b) + c
print(max(d, e, f, g, h, i))

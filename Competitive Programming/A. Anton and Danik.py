n = int (input())
s = input()

a = 0
d = 0

for char in s:
    if char == 'A':
        a += 1
    else:
        d += 1

if a == d:
    print('Friendship')
elif a > d:
    print('Anton')
else:
    print('Danik')
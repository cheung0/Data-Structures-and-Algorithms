n, m = map(int, input().split())

colors = []
for i in range(n):
    l = list(input().split())
    colors.extend(l)

colorful = False
for color in colors:
    if color == 'C' or color == 'M' or color == 'Y':
        colorful = True
        break

if colorful:
    print('#Color')
else:
    print('#Black&White')

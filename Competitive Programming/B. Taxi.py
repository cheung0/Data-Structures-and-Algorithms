n = (int) (input())

l = list(map(int, input().split()))
taxi = 0

four = 0
three = 0
two = 0
one = 0
for element in l:
    if element == 4:
        four += 1
    elif element == 3:
        three += 1
    elif element == 2:
        two += 1
    else:
        one += 1

while four > 0:
    taxi += 1
    four -= 1

while three > 0 and one > 0:
    taxi += 1
    three -= 1
    one -= 1

while two > 1:
    taxi += 1
    two -= 2

while one > 1 and two > 0:
    taxi += 1
    one -= 2
    two -= 1

while one > 0 and two > 0:
    taxi += 1
    one -= 1
    two -= 1

while one > 3:
    taxi += 1
    one -= 4

while one > 2:
    taxi += 1
    taxi -= 3

while one > 1:
    taxi += 1
    taxi -= 2

while three > 0:
    taxi += 1
    three -= 1

while two > 0 :
    taxi += 1
    two -= 1

while one > 0:
    taxi += 1
    one -= 1

print(taxi)







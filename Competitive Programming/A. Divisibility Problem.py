t = int (input())

for i in range(t):
    a, b = map(int, input().split())
    moves = 0
    while a % b != 0:
        a += 1
        moves += 1
    print(moves)


matrix = []

for i in range(5):
    l = list(map(int, input().split()))
    matrix.append(l)

one_pos = [0, 0]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            one_pos = [i + 1, j + 1]
            break


if one_pos == [3, 3]:
    print(0)
else:
    moves = abs(3 - one_pos[0])
    moves += abs(3 - abs(one_pos[1]))
    print(moves)


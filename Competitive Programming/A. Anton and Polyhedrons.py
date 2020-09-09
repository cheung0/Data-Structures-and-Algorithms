s = int (input())

face = 0
for i in range(s):
    m = input()
    if m == 'Tetrahedron':
        face += 4
    elif m == 'Cube':
        face += 6
    elif m == 'Octahedron':
        face += 8
    elif m == 'Dodecahedron':
        face += 12
    elif m == 'Icosahedron':
        face += 20
print(face)

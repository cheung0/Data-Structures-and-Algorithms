l = list(map(int, input().split()))
line = input()
t = l[1]
res = []

for i in range(t):
    i = 0
    while i < len(line):
        if line[i] == 'B' and line[i + 1] == 'G':
            res.append('G')
            res.append('B')
            i += 1
        res.append(line[i])
        i += 1

print(res.)
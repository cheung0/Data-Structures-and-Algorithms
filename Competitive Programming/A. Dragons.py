n, s = map(int, input().split())

bonus = []
dragons = []
for i in range(n):
    b, d = map(int, input().split())
    bonus.append(b)
    dragons.append(d)

no = False
i = 0
while i < n:
    dragons.sort()
    if s < dragons.reverse().pop():
        no = True
        break
    dragons.pop()
    i += 1

if no:
    print('NO')
else:
    print('YES')

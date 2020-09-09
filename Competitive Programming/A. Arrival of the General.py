n = input()
l = list(map(int, input().split()))

min = 0
max = 0
minIndex = 0
maxIndex = 0

for i in range(len(l)):
    if l[i] < min:
        min = l[i]
        minIndex = i
    if l[i] > max:
        max = l[i]
        maxIndex = i

swaps = 0
for i in range(minIndex):
    l[i], l[minIndex] = l[minIndex], l[i]
    swaps += 1
for i in range(maxIndex, len(l)):
    l[i], l[maxIndex] = l[maxIndex], l[i]
    swaps += 1
print(swaps)
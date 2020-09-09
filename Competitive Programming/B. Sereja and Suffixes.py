n, m = map(int, input().split())
l = list(map(int, input().split()))

def distinct(index, alist):
    unique = set()
    for i in range(index, len(alist)):
        if alist[i] not in unique:
            unique.add(alist[i])
    return len(unique)

for i in range(m):
    li = int (input())
    print(distinct(li, l))




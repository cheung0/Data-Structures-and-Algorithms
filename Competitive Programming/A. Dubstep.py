m = input()

k = m.split('WUB')

res = ''
for element in k:
    if element != '':
        res += element
        res += ' '
print(res)


m = input()

seen = set()
for char in m:
    seen.add(char)
l = len(seen)
if l % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

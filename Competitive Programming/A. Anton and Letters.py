n = input()

unique = set()
for char in n:
    if char != '{' and char != '}' and char != ' ' and char != ',':
        unique.add(char)
print(len(unique))

a = input()


seen1 = {}

for char in a:
    if char not in seen1:
        seen1[char] = 1
    else:
        seen1[char] += 1

print(seen1)



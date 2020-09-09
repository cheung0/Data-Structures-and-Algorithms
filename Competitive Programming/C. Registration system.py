n = int (input())

database = {}
for i in range(n):
    user = input()

    if user not in database:
        database[user] = 0
        print('OK')

    else:
        database[user] += 1
        print(user + str(database[user]))




with open('users.csv', 'r') as users:
    list_users= []
    for i in users:
        list_users.append(i.strip(';;;\n'))
print(list_users)
with open('hobby.csv', 'r') as hobby:
    list_hobby= []
    for i in hobby:
        list_hobby.append(i.strip(';;;\n'))
print(list_hobby)

def list_new(list_users, list_hobby):
    i = 0
    while i <= len(list_users) and i < len(list_hobby):
        yield list_users[i], list_hobby[i]
        i += 1
    while i < len(list_users):
        yield list_users[i], None
        i+= 1
with open('list_new.txt', 'w', encoding='utf-8') as f:
    for i in list_new(list_users, list_hobby):
        print((i))
        f.write(str(i)+ '\n')
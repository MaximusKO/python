#  задача1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
# задача2
list_in = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digits = []
for i in list_in:

    if '17,5,+5'.find(i) !=-1:
        digits.append(int(i))
list_2 = list(list_in)
list_2[1],list_2[3],list_2[8] = (f"{digits[0]:02d}"),(f"{digits[1]:02d}"),(f"+{digits[2]:02d}")
list_2.insert(1,"")
list_2.insert(3,"")
list_2.insert(5,"")
list_2.insert(7,"")
list_2.insert(12,"")
list_2.insert(14,"")
print(list_2)
print(" ".join(list_2))
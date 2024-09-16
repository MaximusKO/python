#zadacha 4
orig_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
name = []
for i in orig_list :
    name = i.split()[-1]
    print(f'Привет !,{name.capitalize()}')
#zadacha 5
prod_list = [57.8, 46.51, 97, 7, 90.56, 768.37, 455.09, 56.9, 23.3, 18.83, 45, 768.89, 123.45, 76.2, 12.35, 78, 91, 502, 35.12, 7.87]
print("цены на товары",prod_list,id(prod_list))
for i in range(len(prod_list)) :
    rub = int((prod_list[i]) // 1)
    kop = round((prod_list[i]% 1)*100)
    print(f" {rub:02d}руб. , {kop:02d}коп.")
prod_list.sort()
print(id(prod_list),prod_list)
prod_list.reverse()
print(prod_list,id(prod_list))
print(prod_list[:5])
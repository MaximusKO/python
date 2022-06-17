list_odd = list(range(1,1001,2))
list_odd_cube =[]
for i in range(1,1001,2):
    list_odd_cube.append(i**3)
print("список из куба н.ч чисел",list_odd_cube)
sum_digit_odd_cube = 0
summ_digit = 0
for i in range(len(list_odd_cube)):
    while abs(list_odd_cube[i]) > 0:
        digit = list_odd_cube[i] % 10
        sum_digit_odd_cube= sum_digit_odd_cube + digit
        list_odd_cube[i] = list_odd_cube[i]//10
        if (sum_digit_odd_cube)%7 == 0 :
            summ_digit = summ_digit + list_odd_cube[i]
print("сумма чисел ,сумма цифр которых /7 __",summ_digit)
for i in list_odd :
    list_odd_cube_17 = []
    list_odd_cube_17.append(i**3+17)# к каждому элементу списка добавили 17
    print("список кубов чисел + 17 __",list_odd_cube_17)
summ_digit_17 = 0
sum_digit_odd_cube_17 = 0
for i in range(len(list_odd_cube_17)):
        while abs(list_odd_cube_17[i]) > 0:
            digit = list_odd_cube[i] % 10
            sum_digit_odd_cube_17= sum_digit_odd_cube_17 + digit
            list_odd_cube_17[i] = list_odd_cube_17[i]//10
            if (sum_digit_odd_cube_17)% 7 == 0 :
                summ_digit_17 = summ_digit_17 + list_odd_cube_17[i]
print("сумма чисел ,цифры которого /7 и '+17'__",summ_digit_17)


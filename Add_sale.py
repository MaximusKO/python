
with open('bakery.csv', 'w', encoding='utf-8') as bakery:
    while True :
        i= input('add_sale  ')
        bakery.write(str(i)+ '\n')
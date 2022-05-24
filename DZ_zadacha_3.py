i = 1
while i <= 100:
    #print(i,"процент")
    if i % 10 ==1 and i!=11:
        print(i,"процент")
    if 2<= i % 10 <=4 and i!=12 and i!=13 and i !=14 :
            print(i,"процента")
    if 5<= i % 10 <=9 or i % 10 ==0 or i ==11 or i==12 or i==13 or i==14 :
                print(i,"процентов")
    i += 1

duration = int(input("введите промежуток времени в сек. __"))
if duration<=59 :
        print(duration,"сек.")
elif 60<=duration<=3599 :
        print(duration//60,"мин.",duration%60,"сек." )
elif 3600<=duration<=86399 :
        print(duration//3600,"час.",(duration%3600)//60,'мин.',(duration%60)%60,"сек." )
else:
        print(duration//86400,"дн.",(duration%86400)//3600,"час.",(duration%86400)%3600//60,'мин.',((duration%86400)%3600)%60,"сек.")



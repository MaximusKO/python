 #zadacha 3
def name (*args) :
    key_dict = []
    values_dict =[]
    for i in args:
        key_dict.append(i[:1])
        values_dict.append(i)
    print([i for i, x in enumerate(key_dict) if key_dict.count(x) > 1]) #элементы с одинаковым ключом
    for k, v in zip(key_dict, values_dict):
        print(f"{k}: {v}")
name("Иван", "Мария", "Петр", "Илья","Коля","Леонид","Надежда","Ольга","Ирина","Лео")

#Zadacha 4

import random
k = int(input("введите число шуток  ", ))
nouns = random.sample(["автомобиль", "лес", "огонь", "город", "дом"],k)
adverbs =random.sample (["сегодня", "вчера", "завтра", "позавчера", "ночью",],k)
adjectives =random.sample (["веселый", "яркий", "зеленый", "утопичный","мягкий"],k)
for nouns, adverbs, adjectives in zip(nouns, adverbs, adjectives):
    print(f'{nouns} {adverbs} {adjectives}')


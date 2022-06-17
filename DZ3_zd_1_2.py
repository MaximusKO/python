num_translate = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}
print(num_translate.get(input('enter a number from 0 to 10 _')))
# zadacha 2
num_translate_adv = (num_translate.get(input("_",).lower()))
print(num_translate_adv.capitalize())
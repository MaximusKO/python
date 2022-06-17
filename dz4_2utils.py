import requests
import pprint
import json
from decimal import Decimal
id = input('введите индекс валюты  ')
print(id.upper())
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL)
dict_json = json.loads(response.text)
#pprint.pprint(dict_json)
number = Decimal(dict_json['Valute'][f'{id.upper()}']['Value'])
rate = (number.quantize(Decimal("1.00")))
currency_rates = f"Курс {id.upper()} равен {rate} на {dict_json['Date']}"
print(currency_rates)
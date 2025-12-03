# import requests
# api_key = 'a337cd2f4c68621c5516071a'
# base_currency = 'USD'
# url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
# r = requests.get(url)
# if r.status_code == 200:
#     data = r.json()
#     print(data)
# else:
#     print(f'Ошибка: {r.status_code}')

# import requests
# api_key = 'a337cd2f4c68621c5516071a'
# def exchange(amount=1, from_currency='USD', to_currency='KZT'):
#     url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
#     data = requests.get(url).json()
#     rate = data['conversion_rates'][to_currency]
#     return amount * rate
# amount = float(input("Введите сумму в USD: "))
# result_kzt = exchange(amount, 'USD', 'KZT')
# result_rub = exchange(amount, 'USD', 'RUB')
# result_eur = exchange(amount, 'USD', 'EUR')
# print("\n" + "═" * 60)
# print(f"{'КОНВЕРТАЦИЯ $' + str(amount):^60}")
# print("═" * 60)
# print(f"{amount:.2f} USD (Доллар США)\n")
# print("Конвертировано в:")
# print(f"1. {result_kzt:.2f} KZT (Казахстанский тенге)")
# print(f"2. {result_rub:.2f} RUB (Российский рубль)")
# print(f"3. {result_eur:.2f} EUR (Евро)")
# print("═" * 60)

# import requests
# api_key = 'a337cd2f4c68621c5516071a'
# currencies = ['KZT', 'RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'AED', 'INR']
# def exchange(amount=1, from_currency='USD', to_currency='USD'):
#              url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
#              data = requests.get(url).json()
#              rate = data['conversion_rates'][to_currency]
#              return amount * rate, rate
# currencies = ['KZT', 'RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'AED', 'INR']
# print("Доступные валюты:")
# for i, curr in enumerate(currencies, 1):
#     print(f"{i}. {curr}")
# choice = int(input("Выберите валюту: ")) - 1
# selected_currency = currencies[choice]
# amount = float(input(f"Введите сумму в {selected_currency}: "))
# converted_amount, rate = exchange(amount, selected_currency, 'USD')
# print("\n" + "═" * 60)
# print(f"{'КОНВЕРТАЦИЯ В USD':^60}")
# print("═" * 60)
# print(f"{amount:.2f} {selected_currency}")
# print(" " * 25 + "↓")
# print(f"{converted_amount:.2f} USD")
# print(f"\nКурс: 1 {selected_currency} = {rate:.5f} USD")
# print("═" * 60)

# import requests
# api_key = 'a337cd2f4c68621c5516071a'
# def exchange(amount=1, from_currency='USD', to_currency='KZT'):
#      url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
#      response = requests.get(url)
#      if response.status_code != 200:
#         print("Ошибка при запросе к API")
#      data = response.json()
#      rate = data['conversion_rates'][to_currency]
#      converted_amount = amount * rate
#      return converted_amount, rate
# from_curr = input('Введите валюту ИЗ: ').upper()
# to_curr = input('Введите валюту В: ').upper()
# amount = float(input('Введите сумму: '))
# try:
#     converted_amount, rate = exchange(amount, from_curr, to_curr)
# except Exception as e:
#     print(f"Ошибка: {e}")
#     exit()
# print("\n" + "═" * 60)
# print(f"{'КОНВЕРТАЦИЯ ' + from_curr + ' → ' + to_curr:^60}")
# print("═" * 60)
# print(f"{amount:.2f} {from_curr}")
# print(f"Курс: 1 {from_curr} = {rate:.5f} {to_curr}")  # точность до 5 знаков
# print(" " * 25 + "↓")
# print(f"{converted_amount:.2f} {to_curr}")
# print("═" * 60)

# import requests
# api_key = 'a337cd2f4c68621c5516071a'

# def exchange(amount=1, from_currency='USD', to_currency='USD'):
#     url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
#     response = requests.get(url)
#     if response.status_code != 200:
#         print("Ошибка при запросе к API")
#     data = response.json()
#     rate = data['conversion_rates'][to_currency]
#     converted_amount = amount * rate
#     return converted_amount, rate

# prices = {
#     'США': {'value': 50, 'currency': 'USD'},
#     'Казахстан': {'value': 5000, 'currency': 'KZT'},
#     'Россия': {'value': 4500, 'currency': 'RUB'},
#     'Европа': {'value': 45, 'currency': 'EUR'}
# }
# print("Цены в USD:\n" + "═" * 40)

# for country, price_info in prices.items():
#     usd_price, rate = exchange(price_info['value'], price_info['currency'], 'USD')
#     print(f"{country}: {price_info['value']} {price_info['currency']} → {usd_price:.2f} USD (курс: 1 {price_info['currency']} = {rate:.5f} USD)")
# print("═" * 40)

import requests

api_key = 'a337cd2f4c68621c5516071a'

def exchange(amount=1, from_currency='USD', to_currency='USD'):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Ошибка при запросе к API")
    data = response.json()
    if 'conversion_rates' not in data or to_currency not in data['conversion_rates']:
        raise ValueError(f"Валюта {to_currency} не найдена")
    rate = data['conversion_rates'][to_currency]
    converted_amount = amount * rate
    return converted_amount, rate  # возвращаем кортеж

users = [
    {'name': 'Алиса', 'balance_usd': 100},
    {'name': 'Боб', 'balance_usd': 250},
    {'name': 'Виктор', 'balance_usd': 500},
    {'name': 'Галина', 'balance_usd': 150},
    {'name': 'Дмитрий', 'balance_usd': 300}
]

# Конвертация балансов
for user in users:
    user['balance_kzt'], _ = exchange(user['balance_usd'], 'USD', 'KZT')
    user['balance_kgs'], _ = exchange(user['balance_usd'], 'USD', 'KGS')
    user['balance_rub'], _ = exchange(user['balance_usd'], 'USD', 'RUB')

# Вывод таблицы
print("\n" + "═" * 75)
print(f"{'БАЛАНСЫ ПОЛЬЗОВАТЕЛЕЙ В РАЗНЫХ ВАЛЮТАХ':^75}")
print("═" * 75)
print(f"{'Имя':<10} | {'USD':<8} | {'KZT':<11} | {'KGS':<10} | {'RUB':<10}")
print("─" * 75)
for user in users:
    print(f"{user['name']:<10} | {user['balance_usd']:<8.2f} | {user['balance_kzt']:<11.2f} | {user['balance_kgs']:<10.2f} | {user['balance_rub']:<10.2f}")
print("═" * 75)

# Поиск пользователей с максимальным балансом
max_usd = users[0]
max_kzt = users[0]
max_kgs = users[0]
max_rub = users[0]

for user in users[1:]:
    if user['balance_usd'] > max_usd['balance_usd']:
        max_usd = user
    if user['balance_kzt'] > max_kzt['balance_kzt']:
        max_kzt = user
    if user['balance_kgs'] > max_kgs['balance_kgs']:
        max_kgs = user
    if user['balance_rub'] > max_rub['balance_rub']:
        max_rub = user

print(f"\nМаксимальный баланс в USD: {max_usd['name']} ({max_usd['balance_usd']:.2f} USD)")
print(f"Максимальный баланс в KZT: {max_kzt['name']} ({max_kzt['balance_kzt']:.2f} KZT)")
print(f"Максимальный баланс в KGS: {max_kgs['name']} ({max_kgs['balance_kgs']:.2f} KGS)")
print(f"Максимальный баланс в RUB: {max_rub['name']} ({max_rub['balance_rub']:.2f} RUB)")


# import requests
# from config import open_weather_map_api_key
# from pprint import pprint
# from datetime import datetime
# city_name = 'Алматы'
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={open_weather_map_api_key}&lang=ru&units=metric'
# r = requests.get(url)
# print(r.status_code)
# pprint(r.json())

# data = {'base': 'stations',
#  'clouds': {'all': 0},
#  'cod': 200,
#  'coord': {'lat': 43.25, 'lon': 76.95},
#  'dt': 1764599884,
#  'id': 1526384,
#  'main': {'feels_like': -3.05,
#           'grnd_level': 895,
#           'humidity': 86,
#           'pressure': 1026,
#           'sea_level': 1026,
#           'temp': -3.05,
#           'temp_max': -3.05,
#           'temp_min': -3.05},
#  'name': 'Almaty',
#  'sys': {'country': 'KZ',
#          'id': 8818,
#          'sunrise': 1764554669,
#          'sunset': 1764587896,
#          'type': 1},
#  'timezone': 18000,
#  'visibility': 2000,
#  'weather': [{'description': 'mist', 'icon': '50n', 'id': 701, 'main': 'Mist'},
#              {'description': 'smoke',
#               'icon': '50n',
#               'id': 711,
#               'main': 'Smoke'}],
#  'wind': {'deg': 200, 'speed': 1}}

# timezone = data["timezone"]
# sunrise = datetime.utcfromtimestamp(data['sys']['sunrise'] + timezone)
# sunset = datetime.utcfromtimestamp(data['sys']['sunset'] + timezone)
# print("\n========================================")
# print(f"город {data['name']}, {data['sys']['country']}")
# print(f"Координаты: {data['coord']['lat']}, {data['coord']['lon']}")
# print("========================================\n")
# print(f"🌡 Температура:{data['main']['temp']}, ощущается как {data['main']['feels_like']}")
# print(f"Ветер: {data['wind']['speed']}м/с, направление {data['wind']['deg']}°")
# print("Восход:", sunrise.strftime("%H:%M"))
# print("Закат:", sunset.strftime("%H:%M"))
# print(f"Время {datetime.fromtimestamp(data['dt']).strftime('%y-%m-%d %H:%M:%S')}")

# import requests
# from config import open_weather_map_api_key
# from pprint import pprint
# from datetime import datetime, timezone, timedelta
# city_name = input("Введите город: ")
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={open_weather_map_api_key}&lang=ru&units=metric'
# r = requests.get(url)
# data = r.json()
# if data['cod'] != 200:
#     print("Город не найден!")
#     exit()
# city_timezone = data['timezone']
# tz = timezone(timedelta(seconds=city_timezone))
# sunrise = datetime.fromtimestamp(data['sys']['sunrise'], tz)
# sunset = datetime.fromtimestamp(data['sys']['sunset'], tz)
# local_time = datetime.fromtimestamp(data["dt"], tz)
# weather_main = data['weather'][0]['main']
# weather_desc = data['weather'][0]['description']
# print("\n========================================")
# print(f"Город: {data['name']}, {data['sys']['country']}")
# print(f"Координаты: {data['coord']['lat']}, {data['coord']['lon']}")
# print("========================================\n")
# print(f"Температура: {data['main']['temp']}°C")
# print(f"Ощущается как: {data['main']['feels_like']}°C")
# print(f"Ветер: {data['wind']['speed']} м/с, направление {data['wind']['deg']}°")
# print(f"Влажность: {data['main']['humidity']}%")
# print(f"Давление: {data['main']['pressure']} hPa")
# print(f"Восход: {sunrise.strftime('%H:%M')}")
# print(f"Закат: {sunset.strftime('%H:%M')}")
# print(f"Время {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
# print("========================================\n")

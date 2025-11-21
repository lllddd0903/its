# import random
# win_numbers = []
# for _ in range(5):
#     win_numbers.append(random.randint(1, 50))
# input_numbers = []
# print("Ввеите 5 чисел от 1 до 50: ")
# count = 0 
# while count < 5:
#     num = int(input(f"Число {count + 1}: "))
#     input_numbers.append(num)
#     count += 1
# correct = 0
# for num in input_numbers:
#     if num in win_numbers:
#         correct += 1
# print("\nВыигрышные числа:", win_numbers)
# print("Ваши числа:", input_numbers)
# print(f"\nВы угадали {correct} из 5 чисел!")

# import random
# subjects = ['Математика', 'Физика', 'История', 'Английский', 'Биология']
# while True:
#     random.shuffle(subjects)
#     for i, subject in enumerate(subjects, start=1):
#         print(f"{i}. {subject}")
#     answer = input("\nХотите еще расписание? (да/нет): ")
#     if answer != "да":
#         print("Выход из программы.")
#         break

# import random
# import time
# from datetime import datetime
# participants = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# prizes = ['Ноутбук', 'Смартфон', 'Наушники', 'Монитор', 'Клавиатура']
# while participants:
#     winner = random.choice(participants)
#     prize = random.choice(prizes)
#     participants.remove(winner)
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{current_time}] {winner} выиграл(а) {prize}")
#     time.sleep(2)

# import string
# import random
# import time
# chars = string.ascii_letters + string.digits   
# original = ''.join(random.choice(chars) for _ in range(20))
# print(original)
# input("Нажмите Enter, когда будете готовы...")
# start = time.time()
# typed = input("Печатайте здесь: ")
# end = time.time()
# elapsed = end - start
# correct = 0
# for o, t in zip(original, typed):
#     if o == t:
#         correct += 1
# accuracy = (correct / len(original)) * 100
# speed = len(typed) / elapsed
# print(f"\nВремя: {elapsed:.2f} секунд")
# print(f"Правильность: {accuracy:.0f}%")
# print(f"Скорость: {speed:.2f} символов/сек")

# import string
# import random
# all_chars = string.ascii_letters + string.digits + string.punctuation
# while True:
#     length = int(input("Введите длину пароля (минимум 8): "))
#     if length < 8:
#         print("Пароль должен быть не меньше 8 символов.")
#         continue
#     password = ''.join(random.choice(all_chars) for _ in range(length))
#     print(f"\nДлина пароля: {length}")
#     print(f"Пароль: {password}")
#     answer = input("Нравится? (да/нет): ").lower()
#     if answer == "да":
#         break  

# import datetime
# import time
# new_year = datetime.datetime(2025, 1, 1, 0, 0, 0)
# while True:
#     now = datetime.datetime.now()
#     delta = new_year - now
#     if delta.total_seconds() <= 0:
#         print("С Новым Годом!")
#         break
#     days = delta.days
#     hours, remainder = divmod(delta.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     print(f"Дней: {days}, Часов: {hours:02}, Минут: {minutes:02}, Секунд: {seconds:02}", end='\r')
#     time.sleep(1)

# from datetime import datetime
# log = []
# print("Введите действия (введите 'стоп' для выхода):")
# while True:
#     action = input("Действие: ")
#     if action.lower() == "стоп":
#         break
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log.append(f"[{current_time}] {action}")
# print("\nЛог действий:")
# for entry in log:
#     print(entry)
# if log:
#     first_time_str = log[0][1:20]  
#     last_time_str = log[-1][1:20]  

#     first_time = datetime.strptime(first_time_str, "%Y-%m-%d %H:%M:%S")
#     last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")

#     total_time = last_time - first_time
#     print(f"\nОбщее время работы: {total_time}")
# else:
#     print("Действий не было.")

# import random
# cities = ['Алматы', 'Астана', 'Кокшетау', 'Актобе', 'Шымкент', 'Павлодар', 'Усть-Каменогорск']
# used_cities = [] 
# score = 0
# current_city = random.choice(cities)
# used_cities.append(current_city)
# print(f"Компьютер выбрал: {current_city}")
# score += 1
# while True:
#     last_letter = current_city[-1].lower()
#     user_city = input(f"Назовите город на '{last_letter.upper()}': ").strip()
#     if user_city not in cities or user_city in used_cities or user_city[0].lower() != last_letter:
#         print("Неправильный ответ. Игра окончена!")
#         break
#     used_cities.append(user_city)
#     score += 1
#     possible_cities = [c for c in cities if c[0].lower() == user_city[-1].lower() and c not in used_cities]
#     if not possible_cities:
#         print("Компьютеру больше нечего выбрать. Игра окончена!")
#         break
#     current_city = random.choice(possible_cities)
#     used_cities.append(current_city)
#     print(f"Компьютер выбрал: {current_city}")
#     score += 1
# print(f"\nВы сыграли {score} город(а/ов).")

# import string
# import random
# from datetime import datetime
# name = input("Введите свое имя: ").strip()
# now = datetime.now()
# date_str = now.strftime("%d-%m-%Y")
# time_str = now.strftime("%H:%M:%S")
# def generate_nickname(name):
#     chars = string.ascii_letters + string.digits
#     random_part = ''.join(random.choice(chars) for _ in range(5))
#     return name + random_part
# while True:
#     nickname = generate_nickname(name)
#     print("\n=== ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ===")
#     print(f"Имя: {name}")
#     print(f"Никнейм: {nickname}")
#     print(f"Дата регистрации: {date_str}")
#     print(f"Время: {time_str}")
#     answer = input("\nХотите другой никнейм? (да/нет): ").strip().lower()
#     if answer != "да":
#         break

# import time
# import random
# from datetime import datetime
# customers = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий', 'Евгений']
# start_queue = time.time()
# for customer in customers:
#     start_time = datetime.now().strftime("%H:%M:%S")
#     print(f"[{start_time}] {customer} начинает обслуживание")
#     service_time = random.randint(1, 5)
#     time.sleep(service_time) 
#     end_time = datetime.now().strftime("%H:%M:%S")
#     total_wait = time.time() - start_queue
#     print(f"[{end_time}] {customer} завершила обслуживание ({service_time} сек)")
#     print(f"Время ожидания в очереди: {total_wait:.2f} сек\n")
# end_queue = time.time()
# total_work = (end_queue - start_queue) / 60  
# print("Касса закрыта")
# print(f"Общее время работы: {total_work:.2f} минут")

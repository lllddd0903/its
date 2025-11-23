try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    op = input("Введите операцию (+, -, *, /): ")
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        raise ValueError("Операция не существует")
except ValueError as e:
    print("Ошибка ввода:", e)
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
else:
    print("Результат:", result)
    print("Спасибо за использование!")
finally:
    print("Калькулятор закрыт")

numbers = [10, 20, 30, 40, 50]
while True:
    try:
        a = int(input("Введите индекс: "))
        print("Элемент: ", numbers[a])
    except ValueError as e:
        print("Ошибка ввода:", e)
    except IndexError as e:
        print('Вы ввели не существующий индекс')
    choice = input("Хотите ввести еще инденск? (да/нет): ").strip().lower()
    if choice != "да":
        print("До свидания!")
        break

match =  {'Алиса': 85, 'Боб': 92, 'Виктор': 78, 'Галина': 95}
while True:
    name = input("Введите имя студента: ")
    try:
        print(f"Оценка {name}: {match[name]}")
    except KeyError:
        print("Студент не найден")

    choice = input("Хотите ли поискать еще? (да/нет): ").strip().lower()
    if choice != "да":
        print("Спасибо за использование системы!")
        break

filename = input("Введите имя файла: ")
try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()

    print("Содержимое файла:")
    for line in content:
        print(line.strip())
    print("Количество строк:", len(content))
    print("Файл успешно прочитан")
except FileNotFoundError:
    print(f"Ошибка: файла {filename} нет!")
except ValueError as e:
    print('Ошибка: введите имя файла, а не число!')
finally:
    print("Операция завершена")

users = {'user1': 'pass123', 'user2': 'pass456'}
while True:
    try:
        option = int(input("Введите опцию (1=Вход, 2=Выход): "))
        if option not in (1, 2):
            raise ValueError("Некорректная опция")
        if option == 2:
            print("До свидания!")
            break
        login = input("Введите логин: ")
        if login not in users:
            raise KeyError
        password = input("Введите пароль: ")
        if password == users[login]:
            print("Добро пожаловать!")
        else:
            print("Пароль неверный")
    except ValueError:
        print("Ошибка: введите 1 или 2")
    except KeyError:
        print("Ошибка: пользователь не найден")
    finally:
        print("---")

        
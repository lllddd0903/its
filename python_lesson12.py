def multiply(a, b):
    return a * b
print(multiply(3, 4))
print(multiply(5, 6))
print(multiply(2, 9))

def greet(name, greeting='Привет'):
    return f"{greeting}, {name}!"
print(greet('Алиса'))
print(greet('Боб', 'Привет'))
print(greet('Виктор', 'Добрый день'))

def info(name, age=18, city='Алматы'):
    return f"{name}, {age}, {city}"
print(info('Алиса'))                       
print(info('Боб', 25))                     
print(info('Виктор', 30, 'Астана')) 

def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3))
print(sum_numbers(5, 10, 15, 20))
print(sum_numbers(1))
print(sum_numbers(100, 200, 300, 400, 500))

def print_items(*args):
    for i, item in enumerate(args, start=1):
        print(f"{i}. {item}")
print(print_items('apple', 'banana', 'cherry'))

def count_strings(*args):
    count = 0
    for i in args:
        if isinstance(i, str):
            count += 1
    return count
print(count_strings('hello', 5, 'world', 10, 'test'))

def create_person(**kwargs):
     for key, value in kwargs.items():
        print(f"{key}: {value}")

def introduce(name, age, *hobbies):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print("Хобби:", ", ".join(hobbies))

def show_data(name, *numbers, **info):
        print(f"Имя: {name}")
        if numbers:
            print("Числа:", numbers)
        else:
            print("Числа: нет")
    
        if info:
            print("Информация:")
            for key, value in info.items():
                print(f"{key}: {value}")
        else:
            print("Информация: нет")

def apply_operation(operation, *numbers):
     print(list(map(operation, numbers)))

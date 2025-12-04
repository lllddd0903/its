# #  Задача №1
def multiply(a, b):
    return a * b
print(multiply(5, 3))
print(multiply(10, 2))
print(multiply(-5, 4))

# # Задача №2
def is_odd(n):
    if n % 2 != 0:
        return True
    elif n % 2 == 0:
        return False
print(is_odd(3))
print(is_odd(8))
print(is_odd(11))

# # Задача №3
def count_consonants(text):
    vowels = 'aeiouаеёиоуыэюя'
    count = 0
    for i in text.lower():
        if i.isalpha() and i not in vowels:
            count += 1
    return count
print(count_consonants("hello"))
print(count_consonants("Python"))
print(count_consonants("аэиоу"))

# # Задача №4
def is_anagram(text1, text2):
    t1 = text1.replace('', '').lower()
    t2 = text2.replace('','').lower()
    if len(t1) != len(t2):
        return False
    for i in set(t1):
        if t1.count(i) != t2.count(i):
            return False
    return True
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("abc", "bca")) 

# # Задача №5
def min_three(a, b, c):
    min_number = a
    if b < min_number:
        min_number = b
    elif c < min_number:
        min_number = c
    return min_number
print(min_three(5, 10, 3))
print(min_three(100, 50, 75))
print(min_three(1, 1, 1))

# Задача 11: Подсчет длин слов
# 1. Напишите функцию word_lengths(text)
# 2. Подсчитывает длину каждого слова
# 3. Возвращает словарь {'слово': длина}
#
# Примеры:
# word_lengths("hello world") → {'hello': 5, 'world': 5}
# word_lengths("Python programming") → {'Python': 6, 'programming': 11}
# word_lengths("a") → {'a': 1}

def word_lengths(text):
    word = text.split()
    word_lengths = {}
    for i in word:
        word_lengths[i] = len(i)
    return word_lengths

print(word_lengths("hello world"))
print(word_lengths("Python programming"))
print(word_lengths("a"))


# Задача 12: Декоратор для добавления времени выполнения
# 1. Создайте декоратор measure_time(func)
# 2. Выводит сколько времени выполнялась функция
# 3. Используйте time.time()
#
# Пример:
# @measure_time
# def slow_function():
#     time.sleep(2)
#     return "Done"
#
# slow_function()
# Вывод: Время выполнения: 2.00 секунд
#        Done

import time

def measure_time(func):
    def wappers(*args, **kwarges):
        start_time = time.time()
        result = func(*args, **kwarges)
        end_time = time.time()
        lead_time = end_time - start_time
        print(f'Время выполнения: {lead_time:.2f} секунд')
        return result
    return wappers

@measure_time
def slow_function():
    time.sleep(2)
    return "Done"
slow_function()



# Задача 13: Декоратор для преобразования в верхний регистр
# 1. Создайте декоратор uppercase_result(func)
# 2. Преобразует результат функции в верхний регистр
# 3. Примените к функции message(text)
#
# Пример:
# @uppercase_result
# def message(text):
#     return text
#
# message('hello world') → "HELLO WORLD"
# message('test') → "TEST"

def uppercase_result(func):
    def wappers(*args, **kwarges):
        result = func(*args, **kwarges)
        return result.upper()
    return wappers

@uppercase_result
def message(text):
    return text

print(message('hello world'))
print(message('test'))



# Задача 14: Функция с *args для произведения
# 1. Напишите функцию multiply_all(*args)
# 2. Перемножает все переданные числа
# 3. Используйте цикл или функцию reduce()
#
# Примеры:
# multiply_all(2, 3, 4) → 24
# multiply_all(5, 10) → 50
# multiply_all(1, 1, 1) → 1
# multiply_all(2, 3, 4, 5) → 120

from functools import reduce

def multiply_all_reduce(*args):
    if not args:
        return 1
    return reduce(lambda x, y: x * y, args)

print(multiply_all_reduce(2, 3, 4))
print(multiply_all_reduce(5, 10))
print(multiply_all_reduce(1, 1, 1))
print(multiply_all_reduce(2, 3, 4, 5))


# Задача 15: Функция с *args для конкатенации строк
# 1. Напишите функцию concat_strings(*args)
# 2. Объединяет все строки в одну
# 3. Разделяет пробелом
#
# Примеры:
# concat_strings('Hello', 'World') → "Hello World"
# concat_strings('Python', 'is', 'awesome') → "Python is awesome"
# concat_strings('Test') → "Test"

def concat_strings(*args):
    return ' '.join(args)
print(concat_strings('Hello', 'World'))
print(concat_strings('Python', 'is', 'awesome'))
print(concat_strings('Test'))

# Задача 16
# 1. Напишите функцию show_info(**kwargs)
# 2. Принимает именованные аргументы
# 3. Выводит информацию в формате "ключ: значение"
#
# Пример:
# show_info(name='Алиса', age=20, city='Алматы')
# Вывод:
# name: Алиса
# age: 20
# city: Алматы

# Задача 17
# 1. Создайте декоратор add_suffix(func)
# 2. Добавляет " ✓" в конец результата
# 3. Примените к функции status(text)
#
# Пример:
# @add_suffix
# def status(text):
#     return text
#
status('Ready') → "Ready ✓"
status('Complete') → "Complete ✓"

def start(func):
    a = (f"{func} ✓")
    return a
print(start("Ready"))

# Задача 18
# 1. Напишите функцию is_palindrome_number(num)
# 2. Проверяет является ли число палиндромом
# 3. Например 121 = 121 (палиндром)
#
# Примеры:
# is_palindrome_number(121) → True
# is_palindrome_number(12321) → True
# is_palindrome_number(123) → False
# is_palindrome_number(1) → True

def il(num):
    if num == num[::-1]:
        print("True")
    else:
        print("False")

il("121")
il("123")

# Задача 19
# 1. Создайте декоратор logger(func)
# 2. Логирует название функции, аргументы и результат
# 3. Выводит в формате: "[LOG] Функция: {name}, Аргументы: {args}, Результат: {result}"
#
# Пример:
# @logger
# def add(a, b):
#     return a + b
#
add(5, 3)
Вывод:
[LOG] Функция: add, Аргументы: (5, 3), Результат: 8
Результат: 8

@logger
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
Вывод:
[LOG] Функция: greet, Аргументы: ('Alice',), Результат: Hello, Alice!
Результат: Hello, Alice!

def loger(func):
    def wraper(*args, **kwargs):
        v={
        }
        c = args[0]+args[1]
        v.update(num=args,results=c)
        print (v)
        print(f"Result {c}")
    return wraper

def loger1(func):
    def wraper(*args, **kwargs):
        v={
        }
        c = args
        v.update(num=args,results=c)
        print (v)
        print(f"Result {c}")
    return wraper

@loger
def add(a,b):
    c = a+b
    print(c)
@loger1
def gree(a):
    print(f"Hello,{a}")

add(4,6)
gree("OLEG")
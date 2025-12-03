#  Задача №1
def multiply(a, b):
    return a * b
print(multiply(5, 3))
print(multiply(10, 2))
print(multiply(-5, 4))

# Задача №2
def is_odd(n):
    if n % 2 != 0:
        return True
    elif n % 2 == 0:
        return False
print(is_odd(3))
print(is_odd(8))
print(is_odd(11))

# Задача №3
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

# Задача №4
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

# Задача №5
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
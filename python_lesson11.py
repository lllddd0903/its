def add(a, b):
    return a + b
print(add(5, 3))      
print(add(10, 20))    
print(add(-5, 5))

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(100))

def is_even(num):
    return num % 2 == 0
print(is_even(4))
print(is_even(7))
print(is_even(10))

def count_vowels(text):
    vowels = "аеиоуя"
    count = 0
    for i in text.lower():
        if i in vowels:
            count += 1
    return count
print(count_vowels("hello"))   
print(count_vowels("Python"))  
print(count_vowels("яблоко"))

def square(x):
    return x * x
print(square(2))
print(square(3))
print(square(5))
print(square(10))

def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("радар"))
print(is_palindrome("уровень"))
print(is_palindrome("привет"))
print(is_palindrome("топот"))

def max_of_two(a, b):
   if a > b:
     return a
   else: 
     return b
print(max_of_two(5, 9))
print(max_of_two(15, 3))
print(max_of_two(10, 10))

def apply_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount
print(apply_discount(1000, 10))
print(apply_discount(500, 20))
print(apply_discount(2500, 15))

def multiply_three(a, b, c):
    return a * b * c
print(multiply_three(2, 3, 4))
print(multiply_three(5, 2, 3))
print(multiply_three(1, 1, 1))
print(multiply_three(7, 0, 5))

def get_age_category(age):
    if age < 13:
        return "Ребенок"
    elif 13 <= age <= 17:
        return "Подросток"
    elif 18 <= age <= 65:
        return "Взрослый"
    else:
        return "Пенсионер"
print(get_age_category(8))
print(get_age_category(15))
print(get_age_category(25))
print(get_age_category(70))
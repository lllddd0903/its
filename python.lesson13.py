def add_prefix(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*, {result}"
    return wrapper
@add_prefix
def greeting(name):
    return f"Привет, {name}!"
print(greeting("Алиса"))

def check_positive(func):
    def wrapper(x):
        if x > 0:
            return func(x)
        else:
            return "Ошибка: число должно быть положительным"
    return wrapper
@check_positive
def square(x):
    return x ** 2
print(square(5))

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase
def send(text):
    return text
print(send('hello world'))

def count_calls(func):
    def wrapper(*args, **kwargs):
        count = [0]
        count[0] += 1
        return func(*args, **kwargs)
    return wrapper
@count_calls
def multiply(a, b):
    return a * b
print(multiply(3, 4))

def add_brackets(func):
   def wrapper (*args, **kwargs):
       result = func(*args, **kwargs)
       return f"[{result}]"
   return wrapper
@add_brackets
def concat(a, b):
     return a + b
print(concat('1', '2'))
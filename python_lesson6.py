num = 0
while num <10:
    if num % 2 != 0:
        print(num)
    num += 1

N = int(input("Введите число: "))
count = 1
while count <= N:
    print(count)
    count += 1

N = int(input("Введите число: "))
while N >= 1:
    print(N)
    N -= 1

N = int(input("Введите число: "))
i = 1
total = 0
while i <= N:
    total += i
    i += 1
print("Сумма чисел ", N, total) 

numbers = [10, 20, 30, 40, 50]
i = 0
while i < len(numbers):
    print(f"Индекс {i}: {numbers[i]}")
    i += 1

words = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
language_of_program = input("Введите язык программирования: ")
i = 0
found = False
while i < len(words):
    if words[i].lower() == language_of_program.lower():
      print("Язык найден. Индекс:", i)
      found = True
      break
    i += 1
if not found:
    print("Язык не найден")

N = int(input("Введите число: "))
i = 1
total = 1
while i <= N:
    total *= i
    i += 1
print("Произведение " , N, "равно:", total)

start = int(input("Введите первое число: "))
end = int(input("Введите второе число: "))
i = start
count = 0
while i <= end:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1
print(count)

password = 'qwerty'
password_input = input("Введите пароль: ")
count = 0
while password_input != password:
    print("Пароль не верный")
    count += 1
    if count == 3:
        print("Доступ запрещен")
        break
else:
    print("Пароль верный!")

num = float(input("Введите число: "))
total = 0
count = 0
while num > 0:
    total += num
    count += 1
print(total)
print(count)

N = int(input("Введите число: "))
while N >= 1:
    print(N)
    N /= 2
with open('text.txt', 'w') as file:
    file.write("Привет МИР\n")
    file.write("PyThOn\n")
    file.write("файлы И ДАННЫЕ\n")
with open('text.txt', 'r') as file:
    original_text = file.read()
upper_text = original_text.upper()
with open('text_upper.txt', 'w') as file:
    print(text.txt)
print(original_text)
print("\nФайл в верхнем регистре (text_upper.txt):")
print(upper_text)

with open('file1.txt', 'w') as f1:
    f1.write("Первый файл")
with open('file2.txt', 'w') as f2:
    f2.write("Второй файл")
with open('file1.txt', 'r') as f1:
    text1 = f1.read()
with open('file2.txt', 'r') as f2:
    text2 = f2.read()
merged_text = text1 + "\n---\n" + text2
with open('merged.txt', 'w') as f:
    f.write(merged_text)
print("Содержимое merged.txt:")
print(merged_text)

with open('words.txt', 'w') as f1:
    f1.write("cat dog cat bird dog dog cat fish bird cat")
with open('words.txt', 'r') as file:
    text = file.read()
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
with open('word_count.txt', 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")
print(text)
print("\nСодержимое word_count.txt:")
with open('word_count.txt', 'r') as file:
    print(file.read())

with open('ages.txt', 'w') as file:
    file.write("10\n15\n20\n25\n30\n35\n40\n45\n50")
with open('ages.txt', 'r') as file:
    ages = file.readlines()
ages = [int(age.strip()) for age in ages]
filtered = []
for age in ages:
    if 25 <= age <= 40:
        filtered.append(age)
with open('filtered_ages.txt', 'w') as file:
    for age in filtered:
        file.write(str(age) + "\n")
print("Содержимое ages.txt:")
with open('ages.txt', 'r') as file:
    print(file.read())
print("Содержимое filtered_ages.txt:")
with open('filtered_ages.txt', 'r') as file:
    print(file.read())


with open('products.txt', 'w') as file:
    file.write("Яблоки: 150\n")
    file.write("Бананы: 200\n")
    file.write("Апельсины: 180\n")
    file.write("Груши: 220\n")
with open('products.txt', 'r') as file:
    lines = file.readlines()
products = {}
for line in lines:
    name, price = line.split(":")     
    products[name.strip()] = int(price.strip())
max_price = -1
max_product = ""
for name, price in products.items():
    if price > max_price:
        max_price = price
        max_product = name
min_price = 10**9
min_product = ""
for name, price in products.items():
    if price < min_price:
        min_price = price
        min_product = name
total = 0
for price in products.values():
    total += price
average_price = total / len(products)
print("Словарь товаров:", products)
print("Самый дорогой товар:", max_product, "-", max_price)
print("Самый дешевый товар:", min_product, "-", min_price)
print("Средняя цена:", average_price)

with open('messy_data.txt', 'w') as file:
     file.write("PYTHON Programming")
     file.write("JavaScript\n")
     file.write("SQL\n")
     file.write("CSS\n")
with open('messy_data.txt', 'r') as file:
    lines = file.readlines()
text = []
for line in lines:
    line = line.lower()      
    line = line.strip()      
    text.append(line)
with open('clean_data.txt', 'w') as file:
    for line in text:
        file.write(line + "\n")
with open('messy_data.txt', 'r') as file:
    print(file.read())
with open('clean_data.txt', 'r') as file:
    print(file.read())

with open('article.txt', 'w') as file:
    file.write("Python — популярный язык программирования.\n")
    file.write("Он используется в веб-разработке, анализе данных, ИИ и многом другом.\n")
    file.write("Изучи Python — откроются большие возможности!")
with open('article.txt', 'r') as file:
    lines = file.readlines()
line_count = len(lines)  
word_count = 0
char_count = 0
no_spaces = 0
for line in lines:
    words = line.split()              
    word_count += len(words)           
    char_count += len(line)           
    no_spaces += len(line.replace(" ", ""))
print(f"Строк: {line_count}, Слов: {word_count}, Символов: {char_count}, Символов без пробелов: {no_spaces}") 

with open('numbers.txt', 'w') as file:
    file.write("1 2 3 2 4 5 1 3 6 2")
with open('numbers.txt', 'r') as file:
    text = file.read()
numbers = text.split()             
numbers = [int(n) for n in numbers] 
unique_numbers = set(numbers)
with open('unique_numbers.txt', 'w') as file:
    for num in unique_numbers:
        file.write(str(num) + "\n")
print("Содержимое numbers.txt:")
print(text)
print("\nКоличество всех чисел:", len(numbers))
print("Количество уникальных чисел:", len(unique_numbers))
print("\nСодержимое unique_numbers.txt:")
with open('unique_numbers.txt', 'r') as file:
    print(file.read())

with open('students_unsorted.txt', 'w') as file:
    file.write("Виктор\nАлиса\nБоб\nГалина\nДмитрий")
with open('students_unsorted.txt', 'r') as file:
    students = file.read().splitlines() 
students.sort()
with open('students_sorted.txt', 'w') as file:
    for student in students:
        file.write(student + "\n")
print("Содержимое students_unsorted.txt:")
with open('students_unsorted.txt', 'r') as file:
    print(file.read())
print("Содержимое students_sorted.txt:")
with open('students_sorted.txt', 'r') as file:
    print(file.read())

import datetime
with open('attendance.txt', 'a') as file:  # 'a' чтобы добавлять новые записи
    while True:
        name = input("Введите имя студента (или 'stop' для выхода): ")
        if name.lower() == 'stop':
            break
        now = datetime.datetime.now()
        timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
        file.write(f"{timestamp} {name}\n")
with open('attendance.txt', 'r') as file:
    lines = file.readlines()
attendance_count = {}
for line in lines:
    name = line.strip().split("] ")[1]
    if name in attendance_count:
        attendance_count[name] += 1
    else:
        attendance_count[name] = 1
max_visits = 0
top_student = ""
for student, count in attendance_count.items():
    if count > max_visits:
        max_visits = count
        top_student = student
print("\nВсе записи посещений:")
for line in lines:
    print(line.strip())
print("\nСтатистика посещений:")
for student, count in attendance_count.items():
    print(f"\nСамый активный студент: {top_student} ({max_visits} посещений)")


fruits = ['banana', 'apple', 'cherry', 'date', 'elderberry']
fruits.sort() 
print(fruits)
fruits[::-1]
print(fruits)
for f in fruits:
    # print(f.upper())
a = 0
words = "aey"
for f in fruits: 
    if f[0] in words:
        a += 1
        print(f)
print("Количество фруктов начинающихся на гласную: ", a)

text = [' hello ', '  world  ', ' python ']
text_2 = []
for f in text:
    f = f.strip()
    f = f.replace(" ", "_")
    f = f.lower()
    text_2.append(f)
print(text_2)

numbers = [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
first_index = numbers.index(5)
print(first_index)
count_numbers = numbers.count(5)
print(count_numbers)
pos = []
for i in range(len(numbers)):
    if numbers[i] == 5:
        pos.append(i)
print(pos)
numbers.remove(5)
print(numbers)

students = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
spisok = 0
for i in range(len(students)):
     print(f"{i+1}. {students[i]}")
for i in range(len(students)):
    if students[i] == "Виктор":
        print(i+1)
        break
students.insert(1, 'Евгений')
print(students)
for i in range(len(students)):
    print(f"{i+1}. {students[i]}")

numb = [2, 4, 6, 8, 10, 12, 15, 18, 20]
n_1 = []
for f in numb:
    n_1.append(f * 5)
n_2 = []
for i in numb:
    n_2.append(i ** 2)
n_3 = []
for a in numb:
    if a % 3 == 0:
        n_3.append(a)
spisok = n_1 + n_2 
print(n_1)
print(n_2)
print(n_3)
print(spisok)

words = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
w_1 = words[0]
for f in words:
    if len(f) > len(w_1):
        w_1 = f 
w_2 = words[0]
for i in words:
    if len(i) < len(w_2):
        w_2 = i  
for a in words:
    print(f"{a} -> первая буква: {a[0]}, последняя буква: {a[-1]}, длина: {len(a)}")
w_3 = []
for b in words:
    w_3.append(b.upper())
count = 0
for c in words:
    if "p" in c.lower():
        count += 1
        print(count)
print(w_1, w_2, w_3)

tablica = []
count = 0
max = 0
for f in range(2, 6):
    tabl = ""
    for i in range (1, 11):
        product = f * i
        tabl += f"{f} * {i} = {product}, "
        tablica.append(product)
        if 20 < product < 30:
            count += 1
        if product > max:
            max = product
    table_str = tabl.rstrip(", ")
    print(f"Таблица {f}: {tabl}")
print("\nКоличество произведений > 20 и < 30:", count)
print("Максимальное произведение:", max)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
count = len(numbers)
print(count)
count_5 = numbers.count(5)
print(count_5)
index = number.index(5)
print(index)
numbers.remove(1)
print(numbers)

phrases = ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
o_phrases = []
for f in phrases:
    if "о" in f.lower():
        o_phrases.append(f)
print(o_phrases)
new_phrases = []
for i in phrases:
    if len(i) > 20:
        new_phrases.append(i)
print(new_phrases)
phrases_replace = []
for c in phrases:
    (phrases_replace.append(c.replace(" ", "_")))
print(phrases_replace)
second_phrases = []
for b in phrases:
    first_word = b.split()[0]
    second_phrases.append(first_word)
print(second_phrases)
word_count = 0
for phrase in phrases:
    words = phrase.split()
    word_count += len(words)
print(word_count)

numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
spisok = []
for f in numbers:
    for l in letters:
        spisok.append(str(f) + l)
print(spisok)
second_spisok = []
for i in range(len(numbers)):
    if i < len(letters):                
        second_spisok.append(f"{numbers[i]}-{letters[i]}")
    else:
        second_spisok.append(f"{numbers[i]}-?")
print(second_spisok)
for pair in second_spisok:
    print(pair)
merged = []
merged.extend(spisok)
merged.extend(second_spisok)
print(merged)
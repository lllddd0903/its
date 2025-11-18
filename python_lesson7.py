# numbers = {5, 2, 8, 2, 5, 1, 9, 2}
# print(numbers)
# print(len(numbers))
# print(5 in numbers)
# print(100 in numbers)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# result = set1.intersection(set2)
# print(result)
# result1 = set1.union(set2)
# print(result1)
# difference = set1 - set2
# print("Пересечение:", result)
# print("Объединение:", result1)
# print("Разность:", difference)

# words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'date']
# fruits = set(words)
# print(fruits)
# print(len(fruits))
# fruits_list = list(fruits)
# print(fruits_list)

# dict = {
#     'name': 'Александр',
#     'age': 20,
#     'city': 'Алматы',
#     'grade': 95
# }
# print(dict)
# print(dict['name'])
# print(dict['age'])
# dict['email'] = "alex@mail.com"
# print(dict)

# spisok = {
#     'name': 'Мария', 
#     'age': 25, 
#     'city': 'Астана', 
#     'job': 'Teacher'
#     }
# spisok['age'] = 26
# spisok['city'] = 'Кокшетау'
# spisok.pop('job')
# print(spisok)

# slovar = {
#     'Python': 8, 
#     'Java': 7, 
#     'C++': 6, 
#     'JavaScript': 9
#     }
# for slo in slovar.keys():
#     print(slo)
# for slov in slovar.values():
#     print(slov)
# for slova, pop in slovar.items():
#     print(f"{slova} - {pop}")
# for slova, pop in slovar.items():
#     if pop >= 8:
#         print(slova)

#  7 задача не смогла решить

# students = {
#     'Алиса': 85,
#     'Боб': 92,
#     'Виктор': 78,
#     'Галина': 95,
#     'Дмитрий': 88
# }
# for name, match in students.items():
#     print(f"{name} - {match}")
# total = 0
# for f in students.values():
#     total += f
# srednee = total/len(students)
# print(srednee)
# name1 = ""
# name2 = ""
# maxmatch = 75
# minmatch = 100
# for name, match in students.items():
#     if match > maxmatch:
#         maxmatch = match
#         name1 = name
#     if match < minmatch:
#         minmatch = match
#         name2 = name
# print(name1, maxmatch)
# print(name2, minmatch)

# words = ['cat', 'dog', 'cat', 'bird', 'dog', 'dog', 'cat', 'fish']
# word_count = {}
# for f in words:
#     if f in word_count:
#         word_count[f] += 1
#     else:
#         word_count[f] = 1
# for word, count in word_count.items():
#     print(f"{word} - {count}")
# unique_words = set(words)
# print(unique_words)
# print(len(unique_words))

# hobbies = {
#     'Алиса': ['рисование', 'музыка', 'спорт'],
#     'Боб': ['программирование', 'игры', 'спорт'],
#     'Виктор': ['музыка', 'кино', 'спорт'],
#     'Галина': ['рисование', 'книги', 'путешествия']
# }
# for name, hobby in hobbies.items():
#     print(f"{name} - {hobby}")
# unique_hobbies = set(hobbies)
# for hobby in hobbies.values():
#     unique_hobbies.update(hobby)
# print(unique_hobbies)
# count = 0
# for hobby in hobbies.values():
#     if 'спорт' in hobby:
#         count += 1
# print(count)
# max_hobby_count = -1
# max_student = ""
# for student, hobby in hobbies.items():
#     if len(hobby) > max_hobby_count:
#         max_hobby_count = len(hobby)
#         max_student = student
# print("Студент с наибольшим количеством хобби:", max_student, "-", max_hobby_count, "хобби")
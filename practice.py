text = [18, 'Александр', 92, True, 'ACTIVE']
age = text[0]
name = text[1]
score = text[2]
active = text[3]
status = text[4]
if age >= 18 and status == "ACTIVE":
    print(" Студент принят")
else:
    print(" Студент не принят")
name_2 = name[0]+"." + "*" * (len(name) -1)
print(name_2)
if score >= 90:
    print("Отличник")
elif score >= 75:
    print("Хорошист")
else:
    print("Нужна помощь")
status_2 = status.lower()
print(status_2)
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def meow(self):
        return f"{self.name} говорит: Мяу!"
cat1 = Cat("Васька", 3, "черный")
cat2 = Cat("Мурка", 5, "белый")
cat3 = Cat("Рыжик", 2, "рыжий")
print(cat1.meow())
print(cat2.meow())
print(cat3.meow())

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def study(self):
        return f"{self.name} учится в {self.grade} классе"
student1 = Student("Алиса", 10)
student2 = Student("Боб", 11)
student3 = Student("Кирилл", 9)
print(student1.study())
print(student2.study())
print(student3.study())

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
    def get_info(self):
        return f"{self.name} стоит {self.price}"
    def is_cheap(self):
        if self.price < 100:
            return "Дешево"
        else:
            return "Дорого"
fruit1 = Fruit("Яблоко", 50)
fruit2 = Fruit("Манго", 200)
fruit3 = Fruit("Банан", 90)
print(fruit1.get_info())
print(fruit1.is_cheap())
print(fruit2.get_info())
print(fruit2.is_cheap())
print(fruit3.get_info())
print(fruit3.is_cheap())

class Lamp:
    def __init__(self, brand, is_on):
        self.brand = brand
        self.is_on = is_on
    def turn_on(self):
        self.is_on = True
        return f"{self.brand} включена"
    def turn_off(self):
        self.is_on = False
        return f"{self.brand} выключена"
    def get_status(self):
        if self.is_on == True:
            return "Лампа включена"
        else:
            return "Лампа выключена"
lamp1 = Lamp("Philips", False)
lamp2 = Lamp("Xiaomi", True)
print(lamp1.get_status())
print(lamp1.turn_on())
print(lamp1.get_status())
print(lamp1.turn_off())
print(lamp1.get_status())

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def add_money(self, amount):
#         self.balance += amount
#         return f"{self.owner} пополнил кошелек на {amount}. Балан: {self.balance}"
#     def spend_money(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return f"{self.owner} потратил {amount}. Баланс: {self.balance}"
#         else:
#             return "Недостаточно денег!"
#     def get_balance(self):
#         return f"У {self.owner} есть {self.balance} тенге"
# wallet1 = Wallet("Алиса", 1000)
# wallet2 = Wallet("Боб", 300)
# print(wallet1.get_balance())
# print(wallet1.spend_money(300))
# print(wallet1.get_balance())
# print(wallet1.add_money(500))
# print(wallet1.spend_money(2000))

class Sale:
    def __init__(self, product, tons, price):
        self.product = product
        self.tons = tons
        self.price = price
    def total(self):
        return self.tons * self.price
sale1 = Sale("ТОО Астана ойл", 120, 325000)
sale2 = Sale("ТОО Тобеарал ойл", 325, 264000)
sale3 = Sale("ТОО Новая АЗС", 520, 330000)
total_sales = [sale1, sale2, sale3]
total = 0
for i in total_sales:
    total += i.total()
print("Сумма первой сделки: ", sale1.total())
print("Сумма второй сделки: ", sale2.total())
print("Сумма третьей сделки: ", sale3.total())
print("Общая сумма всех продаж:", total)
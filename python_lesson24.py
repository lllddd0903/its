import math
class Shape:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        return f"{self.name} - это фигура"
    def get_area(self):
        return 0
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def get_info(self):
        return f"{self.name} с радиусом {self.radius}"
    def get_area(self):
        return math.pi * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    def get_info(self):
        return f"{self.name} {self.width}x{self.height}"
    def get_area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
    def get_info(self):
        return f"{self.name} с основанием {self.base} и высотой {self.height}"
    def get_area(self):
        return (self.base * self.height) / 2
circle = Circle("Круг", 5)
rectangle = Rectangle("Прямоугольник", 4, 5)
triangle = Triangle("Треугольник", 6, 3)
print(circle.get_info())
print(rectangle.get_info())
print(triangle.get_info())
print(f"Площадь круга: {circle.get_area():.2f}")
print(f"Площадь прямоугольника: {rectangle.get_area()}")
print(f"Площадь треугольника: {triangle.get_area()}")

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
    def get_info(self):
        return f"{self.name} - {self.position}, зарплата: {self.salary}"
    def get_bonus(self):
        return self.salary * 0.1
class Manager(Employee):
    def __init__(self, name, salary, position, team_size):
        super().__init__(name, salary, position)
        self.team_size = team_size
    def get_info(self):
        return super().get_info() + f" Команда: {self.team_size} человек"
    def get_bonus(self):
        return self.salary * 0.2
class Developer(Employee):
    def __init__(self, name, salary, position, language):
        super().__init__(name, salary, position)
        self.language = language
    def get_info(self):
        return super().get_info() + f" Язык: {self.language}"
    def get_bonus(self):
        return self.salary * 0.15
class Director(Employee):
    def __init__(self, name, salary, position):
        super().__init__(name, salary, position)
    def get_bonus(self):
        return self.salary * 0.3
emp = Employee("Иван", 100000, "Секретарь")
mgr = Manager("Олег", 200000, "Менеджер", 10)
dev = Developer("Мария", 150000, "Разработчик", "Python")
dir = Director("Анна", 300000, "Директор")
employees = [emp, mgr, dev, dir]
for e in employees:
    print(e.get_info())
    print(f"Зарплата: {e.salary}")
    print(f"Бонус: {e.get_bonus()}")
    print(f"Итого с бонусом: {e.salary + e.get_bonus()}")
    print("-" * 40)

class Transport:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
    def get_info(self):  
        return f"{self.brand} {self.model}, макс скорость: {self.max_speed} км/ч"
    def move(self):
        return "Транспортное средство движется"
class Car(Transport):
    def __init__(self, brand, model, max_speed, fuel_type):
        super().__init__(brand, model, max_speed)
        self.fuel_type = fuel_type
    def get_info(self):
        return super().get_info() + f" Топливо: {self.fuel_type}"
    def move(self):
        return f"{self.brand} {self.model} едет по дороге, топливо: {self.fuel_type}"
class Bicycle(Transport):
    def __init__(self, brand, model, max_speed, gear_count):
        super().__init__(brand, model, max_speed)
        self.gear_count = gear_count
    def get_info(self):
        return super().get_info() + f" Передач: {self.gear_count}"
    def move(self):
        return f"{self.brand} {self.model} едет на {self.gear_count} передачах"
class Boat(Transport):
    def move(self):
        return f"{self.brand} {self.model} плывет по воде"
car = Car("Toyota", "Camry", 200, "бензин")
bike = Bicycle("Giant", "Escape", 40, 21)
boat = Boat("Yamaha", "FX Cruiser", 90)
transport = [car, bike, boat]
for i in transport:
    print(i.get_info())
    print(i.move())
    print("-" * 40)
    
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def get_info(self):
        return f"{self.owner}: {self.balance} тенге"
    def get_commission(self):
        commission = self.balance * 0.01
        return commission
    def withdraw(self, amount):
        commission = self.get_commission()
        total = amount + commission
        if total > self.balance:
            print("Недостаточно средств!")
            return
        self.balance -= total
        self.last_commission = commission
    def deposit(self, amount):
        self.balance += amount
        return f"Пополнено на {amount} тенге"
class SavingsAccount(BankAccount):
    def get_commission(self):
        return self.balance * 0.005
    def get_info(self):
        return super().get_info() + " (Сбережения)"
class BusinessAccount(BankAccount):
    def get_commission(self):
        return self.balance * 0.02 
    def get_info(self):
        return super().get_info() + " (Бизнес)"
ac1 = BankAccount("Алиса", 5000)
ac2 = SavingsAccount("Боб", 8000)
ac3 = BusinessAccount("Компания XYZ", 20000)
accounts = [ac1, ac2, ac3]
for ac in accounts:
    print("\n--- Новый счет ---")
    print(ac.get_info())
    ac.deposit(10000)
    print("После пополнения:", ac.get_info())
    ac.withdraw(5000)
    print("После снятия:", ac.get_info())
    print(f"Комиссия за последнюю операцию: {ac.last_commission}")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"{self.name}, {self.age} лет"
    def eat(self):
        return f"{self.name} ест"
    def sleep(self):
        return f"{self.name} спит"
class Walker:
    def move(self):
        return "ходит"
class Swimmer:
    def move(self):
        return "плывет"
class Flyer:
    def move(self):
        return "летает"
    
class Dog(Animal, Walker):
    def get_info(self):
        return super().get_info() + ", может ходить"
    def bark(self):
        return f"{self.name}: Гав-гав!"
class Fish(Animal, Swimmer):
    def get_info(self):
        return super().get_info() + ", может плыть"
class Eagle(Animal, Flyer):
    def get_info(self):
        return super().get_info() + ", может летать"
class Penguin(Animal, Walker, Swimmer):
    def get_info(self):
        return super().get_info() + ", может ходить и плыть"
dog = Dog("Мухтар", 3)
fish = Fish("Немо", 1)
eagle = Eagle("Орлиус", 4)
penguin = Penguin("Полька", 5)
animals = [dog, fish, eagle, penguin]
for a in animals:
    print("\n--- Информация ---")
    print(a.get_info())
    print(a.eat())
    print(a.sleep())
    print("Передвижение:", a.move())
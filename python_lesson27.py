# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.__password = password
#         self.__password_attempts = 0
#         self.__is_blocked = False
#     def get_username(self):
#         return self.username
#     def get_email(self):
#         return self._email
#     def __validate_password(self,password):
#         return password == self.__password
#     def is_account_blocked(self):
#         return self.__is_blocked
#     def unblock_account(self):
#         self.__is_blocked = False
#         self.__password_attempts = 0
#         return "✓ Аккаунт разблокирован администратором"
#     def login(self, password):
#         if self.__is_blocked:
#             return "Аккаунт заблокирован"
#         if self.__validate_password(password):
#             self.__password_attempts = 0
#             return "Успешный вход"
#         self.__password_attempts += 1
#         if self.__password_attempts >= 3:
#             self.__is_blocked = True
#             return "Пароль неверный. Аккаунт заблокирован!"
#         return f"Пароль неверный. Попытка {self.__password_attempts} из 3"
#     def change_password(self, old_password, new_password):
#         if not self.__validate_password(old_password):
#             return " Старый пароль введён неверно"
#         if len(new_password) < 8:
#             return "Новый пароль должен быть не короче 8 символов"

#         self.__password = new_password
#         return "✓ Пароль успешно изменён!"
# user = User("alice", "alice@gmail.com", "password123")
# print(user.login("wrong"))      
# print(user.login("wrong"))      
# print(user.login("wrong"))
# print("\nСтатус блокировки:", user.is_account_blocked())
# print(user.unblock_account())
# print(user.change_password("password123", "newpassword123"))
# print(user.login("newpassword123"))

# from datetime import datetime
# class Product:
#     def __init__(self, name, price, supplier, quantity, min_quantity):
#         self.name = name
#         self.price = price

#         self._suplier = supplier
#         self.__quantity = quantity
#         self.__min_quantity = min_quantity
#         self.__last_update = None

#     def get_quantity(self):
#         return self.__quantity
    
#     def __check_low_stock(self):
#         return self.__quantity <= self.__min_quantity

#     def is_low_stock(self):
#         if self.__check_low_stock():
#             return "Внимание: низкий уровень товара!"
#         return "Товар в наличии"
    
#     def add_stock(self, amount):
#         if amount <= 0:
#             return "Ошибка: количество должно быть больше нуля!"
#         self.__quantity += amount
#         self.__last_update = datetime.now()
#         return f"Добавлено {amount} шт. Текущее количество: {self.__quantity}"
#     def remove_stock(self, amount):
#         if amount <= 0:
#             return "Ошибка: количество должно быть больше нуля!"
#         if amount > self.__quantity:
#             return "❌ Ошибка: недостаточно товара!"
#         warning = ""
#         if self.__quantity - amount <= self.__min_quantity:
#             warning = "Внимание: после снятия количество будет ниже минимума!"
#         self.__quantity -= amount
#         self.__last_update = datetime.now()
#         return f"Снято {amount} шт. Остаток: {self.__quantity} {warning}"
#     def get_info(self):
#         return (
#             f"Название: {self.name}\n"
#             f"Цена: {self.price} тг\n"
#             f"Поставщик: {self._suplier}\n"
#             f"Количество: {self.__quantity}\n"
#             f"Минимум: {self.__min_quantity}\n"
#             f"Последнее обновление: {self.__last_update}\n"
#         )           
# laptop = Product("Ноутбук", 500000, "Dell", 5, 2)

# print(laptop.add_stock(10))        
# print(laptop.get_quantity())       

# print(laptop.remove_stock(12))     
# print(laptop.is_low_stock())       

# print(laptop.remove_stock(100))    

# print(laptop.get_info())    

# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id

#         self._grades = []

#         self.__gpa = 0
#         self.__is_passed = False

#     def __calculate_gpa(self):
#         if len(self._grades) == 0:
#             self.__gpa = 0
#         else:
#             self.__gpa = sum(self._grades)/len(self._grades)

#     def __check_passed(self):
#         self.__is_passed = self.__gpa >= 50        

#     def add_grade(self, grade):
#         if grade < 0 or grade > 100:
#             return "Ошибка: оценка должна быть от 0 до 100!"
#         self._grades.append(grade)
#         self.__calculate_gpa()
#         self.__check_passed()

#     def get_gpa(self):
#         return self.__gpa

#     def get_grades(self):
#         return self._grades.copy()
    
#     def is_passed(self):
#         return "Сдал!" if self.__is_passed else "Не сдал"
    
#     def get_report(self):
#         return (
#             f"Студент: {self.name}\n"
#             f"ID: {self.student_id}\n"
#             f"Оценки: {self._grades}\n"
#             f"GPA: {self.get_gpa()}\n"
#             f"Статус: {self.is_passed()}"
#         )

# student = Student("Алиса", 101)
# student.add_grade(85)
# student.add_grade(92)
# student.add_grade(78)
# student.add_grade(88)
# print(student.get_gpa())      
# print(student.is_passed())    
# print(student.get_report())
    
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, name, age, habitat):
#         self.name = name
#         self.age = age
#         self.habitat = habitat

#     @abstractmethod    
#     def feed(self):
#         pass

#     @abstractmethod
#     def make_sound(self):
#         pass

#     @abstractmethod
#     def get_habitat_info(self):
#         pass

# class Lion(Animal):
#     def feed(self):
#         return f"{self.name} ест 5 кг мяса в день"
#     def make_sound(self):
#         return f"{self.name} рычит: РРРРР!"
#     def get_habitat_info(self):
#         return f"Лев {self.name} живет в {self.habitat}, нужна тень и прохлада"

# class Elephant(Animal):
#     def feed(self):
#         return f"{self.name} ест 200 кг растений в день"
#     def make_sound(self):
#         return f"{self.name} трубит: ТУ-У-У!"
#     def get_habitat_info(self):
#         return f"Слон {self.name} живет в {self.habitat}, нужна вода для ванн"

# class Penguin(Animal):
#     def feed(self):
#         return f"{self.name} ест 500г рыбы в день"
#     def make_sound(self):
#         return f"{self.name} кричит: КР-КР-КР!"
#     def get_habitat_info(self):
#         return f"Пингвин {self.name} живет в {self.habitat}, нужен лед и холод"

# class Snake(Animal):
#     def feed(self):
#         return f"{self.name} ест 1 мышь один раз в неделю"
#     def make_sound(self):
#         return f"{self.name} шипит: Ссссс!"
#     def get_habitat_info(self):
#         return f"Змея {self.name} живет в {self.habitat}, нужна тепловая лампа"
    
# elephant = Elephant("Дамбо", 15, "Саванна")
# lion = Lion("Лео", 8, "Саванна")
# penguin = Penguin("Пингви", 5, "Льды")
# snake = Snake("Сли", 3, "Террариум")

# animals = [elephant, lion, penguin, snake]

# for animal in animals:
#     print(f"=== {animal.name} ===")
#     print(animal.feed())
#     print(animal.make_sound())
#     print(animal.get_habitat_info())
#     print()


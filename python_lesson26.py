# class Notification:
#     def __init__(self, title, message):
#         self.title = title
#         self.message = message
# class EmailNotification(Notification):
#     def send(self):
#         return f'Email: {self.title} | {self.message}'
# class SMSNotification(Notification):
#     def send(self):
#         return f"SMS: {self.title} {self.message}"
# class PushNotification(Notification):
#     def send(self):
#         return f"Push: 🔔 {self.title} - {self.message}"
# class TelegramNotification(Notification):
#     def send(self):
#         return f"Telegram: {self.title}\n{self.message}"
# email = EmailNotification("Новый заказ", "У вас новый заказ #123") 
# sms = SMSNotification("Подтверждение", "Код: 12345") 
# push = PushNotification("Скидка", "Скидка 50% на все товары") 
# telegram = TelegramNotification("Напоминание", "Не забудьте о встречи!")
# notifications = [email, sms, push, telegram] 
# for notification in notifications: 
#     print(notification.send())

# class Payment:
#     def __init__(self, amount, discription):
#         self.amount = amount
#         self.discription = discription
#     def process(self):
#         pass
#     def get_info(self):
#         pass
# class CreditCardPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге обработан кредитной картой"
#     def get_info(self):
#         return f"Кредитная карта: {self.amount} тенге - {self.discription}"
# class MobileWalletPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге обработан мобильным кошельком"
#     def get_info(self):
#         return f"Мобильный кошелек: {self.amount} тенге - {self.discription}"
# class BankTransferPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге переведен банком"
#     def get_info(self):
#         return f"Банковский перевод: {self.amount} тенге - {self.discription}"
# class CryptoPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге принят в крипто"
#     def get_info(self):
#         return f"Крипто: {self.amount} тенге - {self.discription}"
# payment1 = CreditCardPayment(5000, "Покупка товара")
# payment2 = MobileWalletPayment(2000, "Пополнение счета")
# payment3 = BankTransferPayment(10000, "Зарплата")
# payment4 = CryptoPayment(3000, "Инвестиция")
# payments = [payment1, payment2, payment3, payment4]
# for payment in payments:
#     print(payment.get_info())
#     print(payment.process())
#     print()
# total = 0
# for p in payments:
#     total += p.amount
# print(f"Общая сумма платежей: {total} тенге")

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         pass
#     def eat(self, food):
#         pass
#     def get_info(self):
#         pass
# class Lion(Animal):
#     def speak(self):
#         return f"{self.name} рычит: РРРРР!"
#     def eat(self, food):
#         if food == "мясо":
#             return f"{self.name} ест {food}"
#         else:
#             return f"{self.name} не будет есть {food}"
#     def get_info(self):
#         return f"Лев {self.name}, {self.age} лет"
#     def feed(self):
#         return self.eat("мясо")
# class Elephant(Animal):
#     def speak(self):
#         return f"{self.name} трубит: ТУ-У-У!"
#     def eat(self, food):
#         if food == "трава":
#             return f"{self.name} ест {food}"
#         else:
#             return f"{self.name} не будет есть {food}"
#     def get_info(self):
#         return f"Слон {self.name}, {self.age} лет"
#     def feed(self):
#         return self.eat("траву")
# class Parrot(Animal):
#     def speak(self):
#         return f"{self.name} кричит: Привет! Привет!"
#     def eat(self, food):
#         if food == "семечки":
#             return f"{self.name} ест {food}"
#         else:
#             return f"{self.name} не ест {food}"
#     def get_info(self):
#         return f"Попугай {self.name}, {self.age} лет"
#     def feed(self):
#         return self.eat("семечки")
# class Monkey(Animal):
#     def speak(self):
#         return f"{self.name} прыгает и кричит: УУУ-УУУ!"
#     def eat(self, food):
#         if food == "фрукты":
#             return f"{self.name} ест {food}"
#         else:
#             return f"{self.name} не ест {food}" 
#     def get_info(self):
#         return f"Обезьяна {self.name}, {self.age} лет"
#     def feed(self):
#         return self.eat("фрукты")
# lion = Lion("Лео", 5) 
# elephant = Elephant("Дамбо", 10) 
# parrot = Parrot("Кеша", 3) 
# monkey = Monkey("Чита", 4)
# animals = [lion, elephant, parrot, monkey]
# for a in animals:
#     for animal in animals:
#         print(animal.get_info())
#         print(animal.speak())
#         print(animal.feed())   
#         print()

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def get_info(self):
        pass
    def update_gpa(self, new_gpa):
        self.new_gpa = new_gpa
class Course:
    def __init__(self, name, instructor, max_students):
        self.name = name
        self.instructor = instructor
        self.max_students = max_students
        self.students = []
def add_student(self, student):
    if len(self.students) >= self.max_students:
        return f"Курс '{self.name}' уже заполнен!"
    else:
        self.students.append(student)
        return f"Студент {student.name} добавлен"
def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return f"Студент {student.name} удалён из курса {self.name}"
def is_full(self):
    return len(self.students) >= self.max_students

def get_students_count(self):
    return len(self.students)

def show_students(self):
        if not self.students:
            return "На курсе нет студентов."
        return "\n".join(s.get_info() for s in self.students)

def get_average_gpa(self):
        if not self.students:
            return 0
        return round(sum(s.gpa for s in self.students) / len(self.students), 2)

class University:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def find_course(self, course_name):
        for course in self.courses:
            if course.name == course_name:
                return course
        return None

    def get_statistics(self):
        total_courses = len(self.courses)
        total_students = sum(len(c.students) for c in self.courses)
        avg_gpa_all = []

        for c in self.courses:
            if c.students:
                avg_gpa_all.append(c.get_average_gpa())

        university_gpa = round(sum(avg_gpa_all) / len(avg_gpa_all), 2) if avg_gpa_all else 0

        return (
            f"Университет: {self.name}\n"
            f"Всего курсов: {total_courses}\n"
            f"Всего студентов: {total_students}\n"
            f"Средний GPA по университету: {university_gpa}"
        )
uni = University("КазНУ имени аль-Фараби")

python_course = Course("Python", "Иван Петров", 30)
java_course = Course("Java", "Мария Сидорова", 25)
js_course = Course("JavaScript", "Пётр Иванов", 20)

uni.add_course(python_course)
uni.add_course(java_course)
uni.add_course(js_course)
students = [
    Student("Алиса", 1, 4.5),
    Student("Боб", 2, 3.8),
    Student("Карина", 3, 4.2),
    Student("Данил", 4, 2.9),
    Student("Эмир", 5, 3.5),
    Student("Жанна", 6, 4.9),
    Student("Руслан", 7, 3.1),
    Student("Мадина", 8, 4.0),
    Student("Олег", 9, 2.7),
    Student("Тимур", 10, 3.3)
]
python_course.add_student(students[0])
python_course.add_student(students[1])
python_course.add_student(students[2])

java_course.add_student(students[3])
java_course.add_student(students[4])
java_course.add_student(students[5])

js_course.add_student(students[6])
js_course.add_student(students[7])
js_course.add_student(students[8])
js_course.add_student(students[9])
print("=== Информация о курсах ===")
for c in uni.courses:
    print(f"\nКурс: {c.name}")
    print(f"Преподаватель: {c.instructor}")
    print(f"Студентов: {c.get_students_count()}")
    print("Список студентов:")
    print(c.show_students())
    print(f"Средний GPA: {c.get_average_gpa()}")
print("\n=== Статистика университета ===")
print(uni.get_statistics())
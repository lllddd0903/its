class Journal:
    def __init__(self, title, filename):
        self.title = title
        self.filename = filename
        open(self.filename, "a").close()
    def write_data(self, text):
        with open (self.filename, "a") as file:
            file.write(text + "\n")
    def rewrite_data(self, text):
        with open(self.filename, "w") as file:
            file.write(text + "\n")
    def read_data(self):
        with open(self.filename, "r") as file:
            return file.read()
journal = Journal("Мой дневник", "diary.txt")

journal.write_data("Сегодня я выучил классы в Python")
journal.write_data("Мне это понравилось!")

print(journal.read_data())

journal.rewrite_data("Я начал новый дневник")
print(journal.read_data())
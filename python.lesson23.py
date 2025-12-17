class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def get_info(self):
        return f"{self.name} — {self.price} тг, На складе: {self.stock}"
class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = {}
    def add_product(self, product, quantity):
        if product.stock < quantity:
            print("Недостаточно товара '{product.name}' на складе")
            return
        product.stock -= quantity
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity    
        print(f"✔{quantity} шт. '{product.name}' добавлено в корзину {self.owner}")
    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            print(f"Товар '{product.name}' удалён из корзины {self.owner}")
        else:
            print(f"Товара '{product.name}' нет в корзине!")
    def get_total_price(self):
        total = 0
        for product, qty in self.items.items():
            total += product.price * qty
        return total
    def get_item_count(self):
        total_count = 0
        for qty in self.items.values():
            total_count += qty
        return total_count
    def show_cart(self):
        print(f"\n Корзина: {self.owner}")
        if not self.items:
            print("Корзина пустая")
        else:
            for product, qty in self.items.items():
                print(f"- {product.name}: {qty} шт. (Цена: {product.price} тг)")
        print(f"Всего товаров: {self.get_item_count()}")
        print(f"Итого цена: {self.get_total_price()} тг\n")
apple = Product("Яблоко", 50, 100)
milk = Product("Молоко", 300, 50)
bread = Product("Хлеб", 120, 40)
butter = Product("Масло", 700, 20)
cheese = Product("Сыр", 1500, 15)
yogurt = Product("Йогурт", 250, 30)
cart_alice = ShoppingCart("Алиса")
cart_bob = ShoppingCart("Боб")
cart_alice.add_product(apple, 5)
cart_alice.add_product(milk, 2)
cart_alice.add_product(cheese, 1)
cart_bob.add_product(apple, 3)
cart_bob.add_product(bread, 2)
cart_bob.add_product(yogurt, 4)
cart_alice.show_cart()
cart_bob.show_cart()
cart_alice.remove_product(apple)
cart_alice.show_cart()

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def get_info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} - {self.artist} ({minutes:02d}:{seconds:02d})"
class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.songs = []  
        self.current_song_index = 0
    def add_song(self, song):
        self.songs.append(song)
        print(f"✔ Песня '{song.title}' добавлена в альбом '{self.name}'")
    def play(self):
        if not self.songs:
            print("Альбом пустой")
            return
        self.current_song_index = 0
        print(f"▶ Сейчас играет: {self.songs[self.current_song_index].get_info()}")
    def next_song(self):
        if not self.songs:
            print("Альбом пустой")
            return
        if self.current_song_index + 1 < len(self.songs):
            self.current_song_index += 1
            print(f"▶ Сейчас играет: {self.songs[self.current_song_index].get_info()}")
        else:
            print("Вы достигли конца альбома")
    def previous_song(self):
        if not self.songs:
            print("Альбом пустой")
            return
        if self.current_song_index > 0:
            self.current_song_index -= 1
            print(f"◀ Сейчас играет: {self.songs[self.current_song_index].get_info()}")
        else:
            print("Вы на первой песне альбома")
    def show_songs(self):
        if not self.songs:
            print("Альбом пустой")
            return
        print(f"\n🎵 Альбом: {self.name} — {self.artist}")
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. {song.get_info()}")
    def get_total_duration(self):
        total_seconds = 0
        for song in self.songs:
           total_seconds += song.duration
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    def get_current_song(self):
        if not self.songs:
            return "Альбом пустой"
        return self.songs[self.current_song_index].get_info() 
song1 = Song("Speak to Me", "Pink Floyd", 69)
song2 = Song("Breathe", "Pink Floyd", 163)
song3 = Song("Time", "Pink Floyd", 421)
song4 = Song("Money", "Pink Floyd", 382)
album1 = Album("The Dark Side of the Moon", "Pink Floyd")
album1.add_song(song1)
album1.add_song(song2)
album1.add_song(song3)
album1.add_song(song4)

song5 = Song("Come Together", "The Beatles", 259)
song6 = Song("Something", "The Beatles", 182)
song7 = Song("Octopus's Garden", "The Beatles", 171)
song8 = Song("Here Comes The Sun", "The Beatles", 185)

album2 = Album("Abbey Road", "The Beatles")
album2.add_song(song5)
album2.add_song(song6)
album2.add_song(song7)
album2.add_song(song8)

album1.play()
album1.next_song()
album1.next_song()
album1.next_song()
album1.previous_song()
album1.show_songs()
print(f"Общая длительность: {album1.get_total_duration()} минут")
print(f"Сейчас играет: {album1.get_current_song()}")

album2.play()
album2.next_song()
album2.next_song()
album2.previous_song()
album2.show_songs()
print(f"Общая длительность: {album2.get_total_duration()} минут")
print(f"Сейчас играет: {album2.get_current_song()}")


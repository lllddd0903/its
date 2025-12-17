# Задача 1
from abc import ABC, abstractmethod
from datetime import datetime

class Player (ABC):
    def __init__(self, username, player_id, nickname=None):
        self._username = username      
        self._level = 1                 
        self.nickname = nickname or username  

        self.__player_id = player_id    
        self.__rating = 1000            
        self.__matches_played = 0
        self.__wins = 0
    
    @abstractmethod
    def calculate_rating_change(self, victory):
        pass

    @abstractmethod
    def get_skill_bonus(self):
        pass

    @abstractmethod
    def special_ability(self):
        pass

    def get_rating(self):
        return self.__rating

    def get_id(self):
        return self.__player_id
    
    def _update_rating(self, victory, rating_change):
        self.__matches_played += 1
        if victory:
            self.__wins += 1
        self.__rating += rating_change

class Warrior(Player):
    def calculate_rating_change(self, victory):
        return 30 if victory else -15
        
    def get_skill_bonus(self):
        return 5

    def special_ability(self):
        return "Боевой клич! Атака +50%"
    
class Mage(Player):
    def calculate_rating_change(self, victory):
        return 50 if victory else -25
        
    def get_skill_bonus(self):
        return 15

    def special_ability(self):
        return "Магический щит! Защита +100%"

class Archer(Player):
    def calculate_rating_change(self, victory):
        return 40 if victory else -20

    def get_skill_bonus(self):
        return 10

    def special_ability(self):
        return "Дождь стрел! Урон +70%"
    
class Match:
    def __init__(self, match_id, player1, player2, match_type):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.match_type = match_type

        self.__start_time = None
        self.__end_time = None
        self.__winner = None
        self.__is_finished = False 
    def start_match(self):
        self.__start_time = datetime.now()
        print(f"Матч {self.match_id} между {self.player1.nickname} и {self.player2.nickname} начался!")
    def finish_match(self, winner):
        self.__end_time = datetime.now()
        self.__is_finished = True
        self.__winner = winner

        if winner == self.player1:
            self.player1._update_rating(True, self.player1.calculate_rating_change(True))
            self.player2._update_rating(False, self.player2.calculate_rating_change(False))
        elif winner == self.player2:
            self.player2._update_rating(True, self.player2.calculate_rating_change(True))
            self.player1._update_rating(False, self.player1.calculate_rating_change(False))
            
    def get_match_info(self):
        return f"Матч {self.match_id}: {self.player1.nickname} vs {self.player2.nickname}, Победитель: {self.__winner.nickname if self.__winner else 'Еще не завершен'}"

class GameServer:
    def __init__(self, server_name, server_region, max_players):
        self.server_name = server_name
        self.server_region = server_region
    
        self.__players = []
        self.__matches = []
        self.__max_players = max_players

    def register_player(self, player):
        if len(self.__players) >= self.__max_players:
            print("Сервер заполнен!")
            return
        self.__players.append(player)
        print(f"Игрок {player.nickname} зарегистрирован на сервере {self.server_name}.")
    def create_match(self, player1_id, player2_id):
        player1 = next((p for p in self.__players if p.get_id() == player1_id), None)
        player2 = next((p for p in self.__players if p.get_id() == player2_id), None)
        if player1 and player2:
            match_id = len(self.__matches) + 1
            match = Match(match_id, player1, player2, "PvP")
            self.__matches.append(match)
            return match
        print("Ошибка: один или оба игрока не найдены!")
        return None
    def finish_match(self, match_id, winner_id):
        match = next((m for m in self.__matches if m.match_id == match_id), None)
        winner = next((p for p in self.__players if p.get_id() == winner_id), None)
        if match and winner:
            match.finish_match(winner)

    def get_top_players(self, top_n=3):
        sorted_players = sorted(self.__players, key=lambda x: x.get_rating(), reverse=True)
        return [(p.nickname, p.get_rating()) for p in sorted_players[:top_n]]

    def get_server_statistics(self):
        return {
            "Всего игроков": len(self.__players),
            "Всего матчей": len(self.__matches)
        }
warrior = Warrior("Arthur", 1, "Артур")
mage = Mage("Merlin", 2, "Мерлин")
archer = Archer("Robin", 3, "Робин")
warrior2 = Warrior("Lancelot", 4, "Ланселот")
mage2 = Mage("Morgana", 5, "Моргана")

server = GameServer("Dragon Realm", "Европа", max_players=10)

for p in [warrior, mage, archer, warrior2, mage2]:
    server.register_player(p)

match1 = server.create_match(1, 2)
match2 = server.create_match(3, 4)
match3 = server.create_match(5, 1)

match1.start_match()
match2.start_match()
match3.start_match()

server.finish_match(1, 1)  # Артур победил
server.finish_match(2, 4)  # Ланселот победил
server.finish_match(3, 5)  # Моргана победила

for m in server._GameServer__matches:
    print(m.get_match_info())

# Полиморфизм
for p in [warrior, mage, archer, warrior2, mage2]:
    print(f"{p._username} ({p.nickname}): {p.special_ability()}")

print("Топ игроков:", server.get_top_players(3))
print("Статистика сервера:", server.get_server_statistics())  



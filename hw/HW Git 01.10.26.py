import json
# 08  Поиск профиля
# Напишите функцию find_player(player_id). Она должна вернуть словарь игрока или None. 
# Проверьте существующий и отсутствующий id.
# Проверяемый навык: Поиск по идентификатору

def find_player(player_id):
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)
        for player in players:
            if player_id == player["id"]:
                return player
        return None
       
player_exist = find_player(1)  
print(player_exist)      

player_not_exist = find_player(12)
print(player_not_exist)

       


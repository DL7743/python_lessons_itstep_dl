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

# 09  Повышение уровня
# Напишите функцию level_up(player_id), которая увеличивает level на 1, 
# сохраняет изменения и возвращает True. Если игрок не найден, верните False.
# Проверяемый навык: Изменение записи       

def level_up(player_id):
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)
    player_found = False
    for player in players:
        if player_id == player["id"]:
            player["level"] += 1
            player_found = True
            break
    if player_found:
        with open("players.json", "w", encoding="utf-8") as file:
            json.dump(players, file, ensure_ascii=False, indent=4)
        return True
        
    return False
player_exist = level_up(4)  
print(player_exist)      

player_not_exist = level_up(14)
print(player_not_exist)

# 10  Архив профиля
# Напишите функцию deactivate_player(player_id), которая меняет active на False и сохраняет данные. 
# Удалять запись не нужно.
# Проверяемый навык: Мягкое удаление

def deactivate_player(player_id):
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)
    player_found = False
    for player in players:
        if player_id == player["id"] and player["active"] == True:
            player["active"] = False
            player_found = True
            break
    if player_found:
        with open("players.json", "w", encoding="utf-8") as file:
            json.dump(players, file, ensure_ascii=False, indent=4)
        return True
                
    return False

status = deactivate_player(1)
print(status)


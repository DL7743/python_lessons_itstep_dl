import json
# 05  Паспорт Quest Tracker
# • Создайте quest_db.json с ключами next_id и players.
# • Добавьте двух игроков. У каждого должны быть id, nickname, level, inventory и quests.
# • Проверьте файл через json.load и выведите количество игроков.

with open("quest_db.json", "r", encoding="utf-8") as file:
    data = json.load(file)
# data это список который мы прочитали
# так как у нас словарь находится в списке data, то мы заходим в словарь в списке data и 
# достаем список игроков из словаря 
players_list = data[0]["players"]
# теперь мы считаем количество игроков в списке игроков 
count = len(players_list)
# выводим количество игроков 
print(f"Players: {count}")




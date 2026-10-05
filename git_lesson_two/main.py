import json
# 05  Паспорт Quest Tracker
# • Создайте quest_db.json с ключами next_id и players.
# • Добавьте двух игроков. У каждого должны быть id, nickname, level, inventory и quests.
# • Проверьте файл через json.load и выведите количество игроков.

with open("quest_db.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(f"Players: {data["players"]}")




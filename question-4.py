# stdlib
from __future__ import annotations

from datetime import datetime
from datetime import timedelta

from pymongo import MongoClient

from settings import DB_URL
from settings import EXPIRY_TIME
# thirparty
# project

# Вопрос: 	Предложите систему для очистки данных из MongoDB по истечению заданного времени.
# Ответ:    Для достижения желаемого результата можно создать TTL индекс, который удалит документы, у которых поле expireAt указывает на прошедшее время.
# Ссылка:   https://www.mongodb.com/docs/manual/core/index-ttl/


client = MongoClient(DB_URL)
db = client['test_db']
collection = db['test_collection']


collection.create_index('expire_at', expireAfterSeconds=EXPIRY_TIME)
expire_time = datetime.utcnow() + timedelta(seconds=EXPIRY_TIME)

document = {
    'name': 'Abdunazarov Dior',
    'age': 20,
    'expire_at': expire_time,
}
result = collection.insert_one(document)

print(f'Time of expiry: {expire_time}')

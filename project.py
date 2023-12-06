# Татьяна Шумилова, 11 когорта - дипломный проект, 2 часть

import requests
import configuration
import data

# Создаем зааказ
def create_order (body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_URL, json=body)

# Получаем из JSON-ответа номер трека заказа после его создания
def get_track():
    return create_order(data.CREATE_ORDER_BODY).json()["track"]

# Вспомогательные шаги: печатаем полученный трек заказа, чтобы проверить, что всё работает
track = get_track()
print(track)

# Поиск созданного заказа в базе данных
def get_order_from_database():
    return requests.get(configuration.BASE_URL+configuration.GET_ORDER_URL+"track")

# Вспомогательные шаги: печатаем код ответа на запрос
status = get_order_from_database()
print(status)

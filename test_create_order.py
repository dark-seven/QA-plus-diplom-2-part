# Татьяна Шумилова, 11 когорта - дипломный проект, 2 часть

import pytest
import data
import project

# Успешное создание заказа - вспомогательный тест
# Его можно не выполнять, но пусть будет, с ним понятнее :)
def test_success_create_order():
    response = project.create_order(data.CREATE_ORDER_BODY)
    assert response.status_code == 201

# Созданный заказ успешно найден в БД
def test_success_find_order():
    response = project.get_order_from_database()
    assert response.status_code == 200
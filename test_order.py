# 48_1_Иванюк Анастасия - финальный проект_инженер по тестированию расширенный
import pytest
from sender_stand_request import create_order, get_order 
from data import order_body

def test_create_and_get_order():
    
    # Создание заказа и сохранение трека
    response = create_order(order_body) 
    track_number = response.json().get("track")

    # Проверка создания заказа
    assert response.status_code == 201, f"Ошибка при создании заказа: {response.text}"
    assert isinstance(track_number, int), "Сервер не вернул числовой трек!"

    # Получение трека
    order_response = get_order(track_number)

    # Проверка ответа
    assert order_response.status_code == 200, f"Не удалось получить заказ по треку ({track_number}): Код {order_response.status_code}, ответ: {order_response.text}"
    print("Тест пройден!")
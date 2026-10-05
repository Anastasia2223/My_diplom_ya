
import configuration
import requests

# Создание заказа
def create_order(body):
    return requests.post(
        url=configuration.BASE_URL + configuration.ORDERS_ENDPOINT,
        json=body
    )

# Получение заказа по треку
def get_order(track_number):
    # Собираем полный URL вручную
    url = f"{configuration.BASE_URL}{configuration.ORDER_TRACK_ENDPOINT}?t={track_number}"
    response = requests.get(url)
    return response
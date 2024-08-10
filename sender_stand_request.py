import configuration
import data
import requests

# Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDER,
                         json=body)

# Запрос на получение трэк номера заказа
def get_track_id(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

# Тест, который проверяет, что по треку заказа можно получить данные о заказе
def test_order_creation():
    response = post_new_order(data.order_body)
    track_number = response.json()["track"]
    order_response = get_track_id(track_number)
    order_data = order_response.json()
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    print("Заказ успешно создан. Трек номер:", track_number)
    print("Информация о заказе:", order_data)

# Ольга Иванова, 19-я когорта — Финальный проект. Инженер по тестированию плюс
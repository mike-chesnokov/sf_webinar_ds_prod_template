# Скрипт flask сервера для предикта
from flask import Flask, request, jsonify

app = Flask(__name__)


# Flask метод для проверки работы сервера, требования:
# Ендпойнт: "/hello"
# На вход: GET запрос со строковым параметром "param"
# На выходе: json с 2мя полями 'result'
#   'result': str, содержащий "SERVER OK"
#   'param': str, содержащий значение параметра "param" (переданного на вход)
#
# Для проверки корректности используем следующие запросы
# (можно через браузер, можно запустить проверочный скрипт "python test_hello.py"):
#
# url = http://localhost:8000/hello?param=
# response = {'param': '', 'result': 'SERVER OK'}
#
# url = http://localhost:8000/hello?param=42
# response = {'param': '42', 'result': 'SERVER OK'}
#
# url = http://localhost:8000/hello?param=python
# response = {'param': 'python', 'result': 'SERVER OK'}


MODEL_FILE = '_webinar_model.pkl'
FEATURE_ORDER_FILE = '_feature_order.pkl'
TEST_DATA_FILE = '_test_data.pkl'

# Загружаем сериализованные объекты
# Обученная модель
# Лист с порядком признаков
# Признаки для тестового датасета


# ******** НИЖЕ НАПИШИТЕ КОД ЗАГРУЗКИ ТРЕХ СЕРИАЛИЗОВАННЫХ ОБЪЕКТОВ
# ........


# ******** НИЖЕ НАПИШИТЕ КОД FLASK МЕТОДА ДЛЯ ПРОВЕРКИ РАБОТЫ СЕРВЕРА
# ........


# Flask Метод для предикта обученной моделью, требования:
# Ендпойнт: "/predict"
# На вход: GET запрос со строковым параметром "obj_id"
#   obj_id - айди объекта из тестовой выборки
# На выходе: json с 3мя полями
#   'prediction': float округленный до 4 знака "round(prediction, 4)", предсказание модели на объекте obj_id
#       или -1 если произошла любая ошибка
#   'obj_id': str, айди объекта поступившего на вход АПИ
#   'response_status': str, содержащий 'OK' если в ответе предсказание и 'ERROR' если произошла любая ошибка
#
# ОБРАТИТЕ ВНИМАНИЕ: в методе должна быть предусмотрена обработка ошибок,
# чтобы запросы с некорректными входными данными отрабатывали и возвращали HTTP статус код 200
# (например можно использовать try-except)
#
# Для проверки корректности используем следующие запросы
# (можно через браузер, можно запустить проверочный скрипт "python test_predict.py"):

# url = http://localhost:8000/predict?obj_id=8740
# response = {'obj_id': '8740', 'prediction': 2.478, 'response_status': 'OK'}
#
# url = http://localhost:8000/predict?obj_id=162
# response = {'obj_id': '162', 'prediction': 2.4255, 'response_status': 'OK'}
#
# url = http://localhost:8000/predict?obj_id=
# response = {'obj_id': '', 'prediction': -1.0, 'response_status': 'ERROR'}
#
# url = http://localhost:8000/predict?obj_id=python
# response = {'obj_id': 'python', 'prediction': -1.0, 'response_status': 'ERROR'}
#
# url = http://localhost:8000/predict?obj_id=-1
# response = {'obj_id': '-1', 'prediction': -1.0, 'response_status': 'ERROR'}
#
# url = http://localhost:8000/predict?obj_id=168
# response = {'obj_id': '168', 'prediction': -1.0, 'response_status': 'ERROR'}


# ******** НИЖЕ НАПИШИТЕ КОД FLASK МЕТОДА ДЛЯ ПРЕДИКТА ОБУЧЕННОЙ МОДЕЛЬЮ
# ........


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Загружаем данные из датасета
X, y = fetch_california_housing(return_X_y=True, as_frame=True)

# добавляем поле "obj_id" чтобы в дальнейшем идентифицировать объект
X['obj_id'] = list(range(X.shape[0]))

# Разбиваем датасет на трейн и тест по заданным параметрам: размера теста и random_state
TEST_SIZE = 0.2
RANDOM_STATE = 7

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=TEST_SIZE,
                                                    random_state=RANDOM_STATE)
print('Data shapes:', X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Обучаем модель LinearRegression из sklearn на трейне
# при этом не забываем удалить из трейна колонку obj_id
model = LinearRegression()
model.fit(X_train.drop(columns=['obj_id']), y_train)

# Делаем предикт на тесте (не забываем удалить колонку obj_id)
# и измеряем ошибку по MSE
y_pred = model.predict(X_test.drop(columns=['obj_id']))
print('MSE on test:', round(mean_squared_error(y_test, y_pred), 6))

# Сериализуем обученную модель с помощью pickle в файл "webinar_model.pkl"
# в папку "src" рядом
MODEL_FILE = '_webinar_model.pkl'
FEATURE_ORDER_FILE = '_feature_order.pkl'
TEST_DATA_FILE = '_test_data.pkl'


# ******** НИЖЕ НАПИШИТЕ КОД СЕРИАЛИЗАЦИИ МОДЕЛИ В ФАЙЛ MODEL_FILE
# ........


# Тестовую часть датасета сериализуем с помощью pickle для использования в дальнейшем
# Формат сохранения тестовых данных - Pandas DataFrame
# (по желанию можно использовать любую другую конструкцию
# python list/dict, numpy array и т.п., учитывая что
# потом из тестовых данных нужно будет доставать признаки)


# ******** НИЖЕ НАПИШИТЕ КОД СЕРИАЛИЗАЦИИ ТЕСТОВЫХ ДАННЫХ В ФАЙЛ TEST_DATA_FILE
# ........


# Сохраним в отдельный файл feature_order - порядок названий признаков в нашем датасете
feature_order = X.columns.tolist()
feature_order.remove('obj_id')
print('Feature order:', feature_order)


# ******** НИЖЕ НАПИШИТЕ КОД СЕРИАЛИЗАЦИИ feature_order В ФАЙЛ FEATURE_ORDER_FILE
# ........

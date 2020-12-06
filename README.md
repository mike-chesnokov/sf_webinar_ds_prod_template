# Проект для практического вебинара DS Prod
Вебинар состоит из одного проекта (задачи) разбитого на несколько заданий,
которые покрывают следующие темы из курса DS Prod:

- Сериализация в python: pickle (модуль `Подготовка модели к Production`) 
- Создание flask приложения (модуль `Модели ML в Production`)
- docker контейнеры (модуль `Контейнеризация приложений`)
- docker-compose (модуль `Сервисная архитектура и оркестрация приложений`)

## Введение
Для нашей задачи мы будем использовать датасет [California Housing](https://scikit-learn.org/stable/datasets/index.html#california-housing-dataset),
включающий в себя данные о стоимости жилья в Калифорнии по округам / районам (“census”).
Данные можно [загрузить через sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing) 
(код загрузки в есть в файле `model_train.py`). 
Целевая переменная в наборе данных - медианная стоимость жилья для округа, 
а признаки - характеристики этих округов. 
Мы разобьем набор данных на обучение и тест 
и будем предсказывать значение целевой переменной на тесте.

Верхнеуровневые бизнес требования в нашей задаче такие - 
ваш коллега хочет получать оценку стоимости округа из тестового набора данных через АПИ, 
при этом ему у него нет самого датасета, а имеется только id округа. 
Коллеге все равно какие признаки вы будете использовать в своей модели, 
ему для решения проблемы важно получать оценку стоимости для конкретного округа.

Разрабатывать АПИ мы будем локально, 
но ваш коллега не находится с вами в одной сети, поэтому 
чтобы любой человек мог использовать АПИ - 
стоит развернуть проект на сервере AWS.


## Пререквезиты для вебинара
### Что установить / настроить
Для работы с проектом локально нужно иметь на своем компьютере:
- Git (установка на Ubuntu `sudo apt-get install git`)
- Pycharm / VSCode для работы с кодом
- docker ([установка](https://docs.docker.com/engine/install/ubuntu/), 
  [мануал](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru))
- docker-compose ([установка](https://docs.docker.com/compose/install/))
- python библиотеки (для локальной работы, не в docker контейнере), 
  лучше установить в новое виртуальное окружение (`venv`):  
```
# Создаем новое виртуальное окружение "my_env" в удобной для вас папке "dir_for_venv"

cd <dir_for_venv>
python3 -m venv my_env

# Активируем виртуальное окружение "my_env"

source my_env/bin/activate

# Проверяем какие пакеты установлены в новом виртуальном окружении

pip list

# Устанавливаем все необходимые пакеты
pip install numpy==1.19.4
pip install pandas==1.1.4
pip install scikit-learn==0.23.2
pip install flask==1.1.2
pip install requests==2.25.0
```

### Клонирование репозитория
Перед началом вебинара нужно сделать fork [репозитория с проектом](https://github.com/mike-chesnokov/sf_webinar_ds_prod_template),
для этого:
- Создать аккаунт на GitHub (если его нет)
- Перейти в репозиторий шаблона проекта на GitHub по ссылке выше 
- Справа сверху будет кнопка “Fork” - нажимаете ее и репозиторий копируется в ваш профиль
- Далее клонируете репозиторий к себе на локальный компьютер, 
  для этого в вашей копии репозитория (ВАЖНО, что в вашей копии не в основной!) 
  нажимаете зеленую кнопку “Code” и выбираете одну из ссылок для клонирования либо по HTTPS, либо по SSH.
  SSH требует настройки ssh ключей, 
  а HTTPS будет просить ввести пароль от вашего github профиля. 

- Какой тип [ссылки выбрать](https://docs.github.com/en/free-pro-team@latest/github/using-git/which-remote-url-should-i-use) 
- Как настроить [ssh ключи](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh)

- у себя на локальном компьютере в любой удобной папке 
  (где вы хотите, чтобы появился этот проект) 
  выполняете команду git clone 
  (строку после git clone можно скопировать из зеленой кнопки “Code”):для HTTPS:
  
```
# для HTTPS
git clone https://github.com/<YOUR_GITHUB_PROFILE>/sf_webinar_ds_prod_template.git

# для SSH
git clone git@github.com:<YOUR_GITHUB_PROFILE>/sf_webinar_ds_prod_template.git
```


### Что повторить

Для быстрого и успешного выполнения заданий на вебинаре рекомендуется повторить 
следующие модули курса:

- `Подготовка модели к Production` (Сериализация python объектов)
- `Модели ML в Production` (flask, uwsgi, nginx)
- `Контейнеризация приложений` (Работа с docker: Dockerfile, build, run)
- `Сервисная архитектура и оркестрация приложений` (Работа с docker-compose)

Дополнительно к материалам курса для повторения можно посмотреть следующие ссылки:

- Пример работы с [pickle](http://zetcode.com/python/pickle/)
- Тьюториалы по flask: [раз](https://flask.palletsprojects.com/en/1.1.x/quickstart/), 
  [два](https://habr.com/ru/post/346306/)
- Тьюториалы по docker: [раз](https://www.youtube.com/watch?v=YFl2mCHdv24&t=463s), 
  [два](https://docker-curriculum.com/)
- Тьюториалы по docker-compose: [раз](https://www.youtube.com/watch?v=Qw9zlE3t8Ko),
  [два](https://habr.com/ru/company/ruvds/blog/450312/), 
  [три](https://www.educative.io/blog/docker-compose-tutorial)
- Примеры flask + uwsgi + docker + nginx: [раз](http://snakeproject.ru/rubric/article.php?art=docker_flask_06.02.2019),
  [два](https://smirnov-am.github.io/running-flask-in-production-with-docker/),
  [три](https://pythonise.com/series/learning-flask/building-a-flask-app-with-docker-compose)


## План решения задачи
Перед началом выполнения заданий предлагается прикинуть примерный 
план решения нашей задачи:
- Какие шаги мы будем проходить?

## Задания
В каждом задании необходимо заполнить недостающие фрагменты кода 
и запустить этот код с помощью команд приведенных ниже. 
Команды запуска можно выполнять как из терминала, так и из IDE.

### 1. Обучение и сериалзизация модели, сериализация данных
Вначале мы загружаем датасет, добавляем айди объекта для использования в дальнейшем.
Разбиваем датасет на трейн и тест - 
на трейне обучаем модель LinearRegression из sklearn.
Для сравнения друг с другом измеряем метрику MSE на тесте. 
Также мы сериализуем саму модель и тест данные 
(таргет с теста не сериализуем, т.к. 
при реальном применении модели у нас не будет ответов на новых данных)
для использования во время инференса модели в дальнейшем.
 
 
Заполните пропуски в файле `/app/src/model_train.py`. 
Команды ниже выполняют обучение модели и сериализацию данных
```
cd <project_directory>/app/src/

python model_train.py 
```
В результате выполнения команд у вас в папке src должны появиться 3 файла:
- `_webinar_model.pkl`
- `_test_data.pkl`
- `_feature_order.pkl`

**ПЕРЕХОДИМ В ФАЙЛ** `/app/src/model_train.py`

### 2. Flask приложение:
В файле server.py будем писать наше фласк приложение с двумя flask методами:
- `/hello` (для проверки работы сервера) - 
принимает get запрос с параметром “param”,
 возвращает строку ОК со значением param переданным в запросе
- `/predict` (для инференса обученной моделью) - 
принимает get запрос с айди объекта,
 возвращает предсказание модели на этом объекте


Заполните пропуски в файле `/app/src/server.py`. 
Команды ниже запускают flask сервер
```
cd <project_directory>/app/src/

python server.py 
```
Протестировать работу API в этом задании можно 
вручную (запросами в браузере, приведены в коде `server.py`) 
или автоматически - запуском скриптов:
```
cd <project_directory>/app/src/

python test_hello.py

python test_predict.py
```

**ПЕРЕХОДИМ В ФАЙЛ** `/app/src/server.py`

### 3. Flask приложение в docker контейнере:
Для обеспечении изолированности окружения нашего приложения 
будем разворачивать проект в docker контейнере, 
для этого используем соответствующий Dockerfile.

Заполните пропуски в файле `/app/flask.Dockerfile`.
Команды ниже выполняют сборку и запуск контейнера с приложением

```
cd <project_directory>/app/

docker build -t webinar_app -f flask.Dockerfile .

docker run -p 8000:8000 -it --rm --name webinar_app webinar_app
```
Тестируем работу API в этом задании можно 
вручную (запросами в браузере, приведены в коде `server.py`) 
или автоматически - запуском скриптов:
```
cd <project_directory>/app/src/

python test_hello.py

python test_predict.py
```

**ПЕРЕХОДИМ В ФАЙЛ** `/app/flask.Dockerfile`

### 4. Flask + uwsgi приложение в docker контейнере:
Для использования нашего python приложения в prod окружении 
необходимо добавить к нему WSGI сервер. 
Для этого соберем в одном контейнере flask + uwsgi приложение.

Заполните пропуски в файле `/app/uwsgi.Dockerfile`.
Команды ниже выполняют сборку и запуск контейнера с приложением
```
cd <project_directory>/app/

docker build -t webinar_app_uwsgi -f uwsgi.Dockerfile .

docker run -p 8000:8000 -it --rm --name webinar_app_uwsgi webinar_app_uwsgi
```
Тестируем работу API в этом задании можно 
вручную (запросами в браузере, приведены в коде `server.py`) 
или автоматически - запуском скриптов:
```
cd <project_directory>/app/src/

python test_hello.py

python test_predict.py
```

**ПЕРЕХОДИМ В ФАЙЛ** `/app/uwsgi.Dockerfile`

### 5. Flask + uwsgi приложение и nginx в двух разных контейнерах:
Для дальнейшей подготовки нашего приложения к prod окружению 
нам стоит добавить сервер Nginx в нашу систему. Развернем Nginx 
в отдельном контейнере рядом с контейнером приложения flask + uwsgi. 
Всю систему целиком мы будем собирать и поднимать через docker-compose.

Заполните пропуски в файле `docker-compose.yml`.
Команда ниже выполняет сборку и запуск контейнеров с приложением
```
docker-compose up --build
```
Тестируем работу API в этом задании можно 
вручную (запросами в браузере, приведены в коде `server.py`) 
или автоматически - запуском скриптов:
```
cd <project_directory>/app/src/

python test_hello.py

python test_predict.py
```

**ПЕРЕХОДИМ В ФАЙЛ** `docker-compose.yml`

## Заключение

Вы великолепны!

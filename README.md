# Интерактивная карта Москвы с местами для отдыха

## Как установить

Python 3.8 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Создайте файл `.env` в корневой директории проекта и добавьте переменные окружения:


-   ALLOWED_HOSTS=смотреть [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
-   SECRET_KEY=Ваш секретный ключ для django
-   DEBUG_DJANGO=true или false


## Как запустить
Для создания таблиц проведите миграции
```
python manage.py makemigrations
python manage.py migrate
```
Для запуска веб сервера
```
python manage.py runserver
```
Для входа в админку создайте учётную запись
```
python manage.py createsuperuser
```
И авторизуйтесь http://127.0.0.1:8000/admin/

## Демо сайта
[Демо](https://technician03.pythonanywhere.com/) \
[Админка](https://technician03.pythonanywhere.com/admin/)
```
Логин: admin
Пароль: admin
```

## Загрузка мест из json файла
[Пример json файла](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json)
```
python manage.py load_place http://адрес/файла.json
```
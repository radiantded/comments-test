# Тестовое задание Комментарии API

## Развертывание и запуск проекта

1. Клонируйте репозиторий проекта:
```
git clone https://github.com/radiantded/comments-test.git
```
2. Создайте и запустите виртуальное окружение в директории с проектом:
```
cd {директория проекта}
python -m venv venv
source venv/bin/activate (для Linux)
source venv/Scripts/activate (для Windows)
```
3. Создайте файл .env со следующими переменными окружения:
```
SECRET_KEY = '{ключ Django}'
DB_ENGINE = 'django.db.backends.postgresql'
DB_NAME = '{имя БД}'
PG_USER = '{пользователь}'
PG_PASS = '{пароль}'
DB_HOST = '{хост, по умолчанию localhost}'
DB_PORT = '{порт, по умолчанию 5432}'
```
4. Установите зависимости:
```
pip install -r requirements.txt
```
5. Запустите проект:
```
python manage.py runserver
```
6. Swagger будет доступен по адресу http://127.0.0.1:8000/api/v1/doc

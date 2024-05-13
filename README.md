# Проект "Вангер тестовое"

Работа над проектом «Тестовое задание Вангер".

## Технический стек:
- [Python 3.9.10](https://docs.python.org/release/3.9.10/)
- [Django 4.1](https://docs.djangoproject.com/en/4.1/)
- [MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/)

## Запуск проекта:
+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```shell script
python -m venv venv
```

```shell script
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```shell script
python -m pip install --upgrade pip
```

```shell script
pip install -r backend/requirements.txt
```

+ Выполнить миграции:
```shell script
python manage.py migrate
```

+ Запустить проект:
```shell script
python manage.py runserver
```



[GitHub](https://github.com/TheDoBa) | Разработчик - Vladimir Avizhen

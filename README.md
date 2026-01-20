Инициализация алембика
```
cd app
```
```shell
  alembic init -t async migration
```

Переносим alembic.ini в корневую папку.
Открываем alembic.ini и изменяем путь к папке миграций:
```
script_location = migration -> script_location = app/migration
```

Генерация миграций(предварительно создайте папку data в корневом пути)
```shell
    alembic revision --autogenerate -m "Initial revision"
```

Выполнение миграций и создание таблиц БД
```shell
    alembic upgrade head
```
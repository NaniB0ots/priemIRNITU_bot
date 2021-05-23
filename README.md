# priemIRNITU_bot

Чат бот для Вк и telegram "Приемная комиссия ИРНИТУ" для отображения информации для поступающих


## Запуск проекта 
##### ОС Ubuntu
##### *Должны быть установлены* `Docker` *и* `docker-compose`

1. Создать файл `.env.db` в котором указать (пример файл `.env.db.example`):
    - `POSTGRES_USER=pg_user`
    - `POSTGRES_PASSWORD=pg_password`
    - `POSTGRES_DB=database`
3. Создать файл `.env` в котором указать (пример файл `.env.example`):
    - `DEBUG=off`
    - `SECRET_KEY=your-secret-key`
    - `DATABASE_URL=psql://<pg_user>:<pg_password>@db:5432/<database>`
    - `TG_TOKEN=your-token`
    - `VK_TOKEN=your-token`
    
3. Запустить проект `$ docker-compose up -d --build`
4. Проверить статус контейнеров `$ docker-compose ps`
5. Настроить базу данных `$ docker exec -it <priemirnitu_bot_db_1> psql -U <pg_user> -d <database> -c "CREATE EXTENSION pg_trgm;"`
6. Созадть суперпользователя `$ docker exec -it <priemirnitu_bot_web_1> python manage.py createsuperuser`
7. Перейти на http://<host_name>/admin и создать группы пользователей и пользователей

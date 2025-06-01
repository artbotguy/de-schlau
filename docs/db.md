

ERRORS

    ERROR [flask_migrate] Error: Can't locate revision identified by '73d05cd4462a':
        docker-compose exec web flask db init
        docker-compose exec web flask db revision --rev-id <REV_ID>         
        docker-compose exec web flask db upgrade


Напрямую к бд:
    docker exec db psql -U myuser -d mydb -c "SELECT * FROM word_pair;"
        #
    docker exec -it db bash
    psql -U myuser -d mydb
    SELECT * FROM word_pair;



Основные команды миграций
    1. Инициализация (первый запуск)
        docker-compose exec web flask db init
        Создает папку migrations с файлами миграций
        

    2. Создание новой миграции (после изменения моделей)
        docker-compose exec web flask db migrate -m "test"
        Генерирует файл миграции в migrations/versions/

    3. Применение миграций
        docker-compose exec web flask db upgrade
        Применяет все непримененные миграции

    4. Откат миграции
        docker-compose exec web flask db downgrade
        Откатывает последнюю примененную миграцию

    🛠️ Дополнительные команды
    Проверка текущего состояния
        docker-compose exec web flask db current
    Просмотр истории миграций
        docker-compose exec web flask db history
    Применение конкретной миграции
        docker-compose exec web flask db upgrade <revision>
    Создание пустой миграции (для ручного SQL)
        docker-compose exec web flask db revision -m "Ручная миграция"
    💡 Полезные алиасы (добавьте в ~/.bashrc)
        alias dmigrate='docker-compose exec web flask db migrate'
        alias dupgrade='docker-compose exec web flask db upgrade'
        alias ddowngrade='docker-compose exec web flask db downgrade'
    🔄 Типичный рабочий процесс
    Измените модели в models.py

    Создайте миграцию:
        docker-compose exec web flask db migrate -m "Добавил поле examples"
    Примените изменения:
        docker-compose exec web flask db upgrade
    Если нужно откатить:
        docker-compose exec web flask db downgrade

    - Важные нюансы
    Все команды выполняются внутри контейнера

    Папка migrations должна быть смонтирована в docker-compose.yml:

    yaml
    volumes:
    - ./migrations:/app/migrations
    Для первого запуска в новом окружении:

    docker-compose exec web flask db upgrade
    - Если миграции не работают
    Проверьте наличие FLASK_APP в окружении:

    docker-compose exec web env | grep FLASK
    Убедитесь, что в app/__init__.py инициализирован Migrate:

    python
    from flask_migrate import Migrate
    migrate = Migrate(app, db)



Выгрузка (как я переделал volume в обычный):
    docker-compose exec db pg_dump -U myuser -d mydb > dump.sql

        # Удалит контейнеры и тома (данные потеряются!)
    docker-compose down -v  
    
    docker cp /Users/abotkin/dev/de-schlau/dump.sql <ваш_контейнер_db>:/tmp/dump.sql

    sudo rm -rf ./postgres_data/*

        #запустили контейнер
    docker-compose up -d db

        # Копируем файл в контейнер
    docker cp /Users/abotkin/dev/de-schlau/dump.sql ваш_контейнер_db:/tmp/dump.sql

        # Загружаем дамп
    docker-compose exec db psql -U myuser -d mydb -f /tmp/dump.sql



RSYNC
    rsync -avz -e "ssh -p 22" ./* root@89.191.225.200:/home/abotkin/dev/de-shlau

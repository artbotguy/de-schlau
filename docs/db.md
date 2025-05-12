

ERRORS

    ERROR [flask_migrate] Error: Can't locate revision identified by '73d05cd4462a':
        docker-compose exec web flask db init
        docker-compose exec web flask db revision --rev-id <REV_ID>         
        docker-compose exec web flask db upgrade



🔄 Основные команды миграций
1. Инициализация (первый запуск) --- СТАРТОВЫЙ ПОИНТ
    docker-compose exec web flask db init
    Создает папку migrations с файлами миграций
    

2. Создание новой миграции (после изменения моделей)
    docker-compose exec web flask db migrate -m "Описание изменений"
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

⚠️ Важные нюансы
Все команды выполняются внутри контейнера

Папка migrations должна быть смонтирована в docker-compose.yml:

yaml
volumes:
  - ./migrations:/app/migrations
Для первого запуска в новом окружении:

docker-compose exec web flask db upgrade
❌ Если миграции не работают
Проверьте наличие FLASK_APP в окружении:

docker-compose exec web env | grep FLASK
Убедитесь, что в app/__init__.py инициализирован Migrate:

python
from flask_migrate import Migrate
migrate = Migrate(app, db)

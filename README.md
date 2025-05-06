# Flask Docker Starter

Проект на Flask с Docker (Gunicorn + Nginx + PostgreSQL)

## Запуск
```bash
docker-compose up --build
```
Приложение будет доступно на http://localhost

## Структура
- `app/` - исходный код Flask-приложения
- `nginx.conf` - конфигурация Nginx
- `Dockerfile` - сборка образа для Flask/Gunicorn
- `docker-compose.yml` - оркестрация сервисов
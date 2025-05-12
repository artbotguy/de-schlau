from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()  # Инициализация без приложения


def create_app():
    app = Flask(__name__, template_folder='templates')

    # Конфигурация
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True,
        SQLALCHEMY_DATABASE_URI='postgresql://myuser:mypassword@db/mydb',
        SQLALCHEMY_TRACK_MODIFICATIONS=False  # Добавлено для подавления предупреждений
    )

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)  # Поздняя инициализация

    # Регистрация Blueprints
    from app.routes import bp, main_bp  # Импорт здесь чтобы избежать circular imports
    app.register_blueprint(bp)
    app.register_blueprint(main_bp)

    # Создание таблиц (только для dev-среды)
    with app.app_context():
        if app.config.get('FLASK_ENV') == 'development':
            db.create_all()

    return app

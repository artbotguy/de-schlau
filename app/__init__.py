from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db/mydb'

    db.init_app(app)
    migrate = Migrate(app, db)

    from app import routes
    app.register_blueprint(routes.bp)
    app.register_blueprint(routes.main_bp)

    with app.app_context():
        db.create_all()

    return app

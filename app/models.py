from app import db
from sqlalchemy import inspect


class WordPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    translation = db.Column(db.String(100))
    examples = db.Column(db.Text, nullable=True)
    cognitive_status = db.Column(
        db.String(100), nullable=True, default="new")  # 'new', 'familiar', 'studied # nullable временно
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<WordPair {self.word}-{self.translation}>'

    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'translation': self.translation,
            'examples': self.examples,
            'cognitive_status': self.cognitive_status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    @classmethod
    def get_editable_fields(cls):
        # Исключаем автоматически генерируемые поля
        excluded_fields = {'id', 'created_at'}
        inspector = inspect(cls)
        return [column.name for column in inspector.columns if column.name not in excluded_fields]

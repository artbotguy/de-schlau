from app import db


class WordPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    translation = db.Column(db.String(100))
    # examples = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<WordPair {self.word}-{self.translation}>'

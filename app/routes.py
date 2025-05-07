from flask import Blueprint, request, jsonify, render_template
from app.models import WordPair
from app import db

bp = Blueprint('words', __name__, url_prefix='/words')


@bp.route('/', methods=['GET'])
def get_words():
    words = WordPair.query.order_by(WordPair.id.desc()).limit(10).all()
    return jsonify([{
        'id': w.id,
        'word': w.word,
        'translation': w.translation
    } for w in words])


@bp.route('/add', methods=['GET', 'POST'])
def add_word():
    if request.method == 'GET':
        return render_template('add_word.html')

    if request.method == 'POST':
        try:
            data = request.get_json()

            if not data or 'word' not in data or 'translation' not in data:
                return jsonify({"error": "Не указано слово или перевод"}), 400

            new_word = WordPair(
                word=data['word'],
                translation=data['translation']
            )
            db.session.add(new_word)
            db.session.commit()

            return jsonify({
                "message": "Слово добавлено!",
                "word": data['word'],
                "translation": data['translation']
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

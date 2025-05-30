from flask import Blueprint, request, jsonify, render_template
from app.models import WordPair
from app import db

bp = Blueprint('words', __name__, url_prefix='/words')

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    words = WordPair.query.paginate(page=page, per_page=per_page)
    return render_template('home.html', words=words)


@bp.route('/', methods=['GET'])
def get_words():
    words = WordPair.query.order_by(WordPair.id.desc()).limit(10).all()
    # return jsonify([{
    #     'id': w.id,
    #     'word': w.word,
    #     'translation': w.translation,
    #     'examples': w.examples,
    #     'cognitive_status': w.cognitive_status
    # } for w in words])
    return render_template('words.html', words=words)


@bp.route('/add', methods=['GET'])
def add_word_form():
    word_id = request.args.get('id')
    word = None

    if word_id:
        word = WordPair.query.get_or_404(word_id)

    editable_fields = WordPair.get_editable_fields()
    return render_template('add_word.html', fields=editable_fields, word=word)


@bp.route('/save', methods=['POST'])
def save_word():
    try:
        data = request.get_json()

        if not data or 'word' not in data:
            return jsonify({"error": "Не указано слово"}), 400

        # Если есть ID - редактируем существующее слово
        if 'id' in data and data['id']:
            word = WordPair.query.get_or_404(data['id'])
            word.word = data['word']
            word.translation = data.get('translation', '')
            word.examples = data.get('examples', '')
            word.cognitive_status = data.get('cognitive_status', 'new')
            message = "Слово обновлено!"
        else:
            # Создаем новое слово
            word = WordPair(
                word=data['word'],
                translation=data.get('translation', ''),
                examples=data.get('examples', ''),
                cognitive_status=data.get('cognitive_status', 'new')
            )
            db.session.add(word)
            message = "Слово добавлено!"

        db.session.commit()

        return jsonify({
            "message": message,
            "word": {
                "id": word.id,
                "word": word.word,
                "translation": word.translation,
                "examples": word.examples,
                "cognitive_status": word.cognitive_status
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# @bp.route('/<int:word_id>', methods=['GET'])
# def get_word(word_id):
#     """Возвращает данные конкретного слова"""
#     word = WordPair.query.get_or_404(word_id)
#     return jsonify({
#         'id': word.id,
#         'word': word.word,
#         'translation': word.translation,
#         'examples': word.examples,
#         'cognitive_status': word.cognitive_status
#     })

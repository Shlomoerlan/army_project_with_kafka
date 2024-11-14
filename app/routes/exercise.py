from flask import jsonify

from app.repository.exercise_repository import get_most_common_words
from app.routes.get_data import app


@app.route('/api/common-words', methods=['GET'])
def common_words_route():
    try:
        words_rank = get_most_common_words()
        return jsonify(words_rank)
    except Exception as e:
        return jsonify({'error': str(e)})


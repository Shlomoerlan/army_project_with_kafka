from app.repository.exercise_repository import get_most_common_words, get_user_by_email, create_user
from flask import jsonify, abort, Flask

app = Flask(__name__)

@app.route('/api/common-words', methods=['GET'])
def common_words_route():
    try:
        words_rank = get_most_common_words()
        return jsonify(words_rank)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/user/<string:email>', methods=['GET'])
def get_user_route(email):
    if not email:
        return abort(400, description="Email parameter is required.")
    try:
        user = get_user_by_email(email)
        if user is None:
            return abort(404, description="User not found.")

        user_data = create_user(user)
        return jsonify(user_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
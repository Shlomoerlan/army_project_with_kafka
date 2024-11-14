from flask import Flask, request, jsonify
from app.utils.selector import selector

app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def receive_email():
    data = request.json
    selector(data)
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    selector(data)
    return jsonify({
        "status": f"Message received",
    }), 200


if __name__ == '__main__':
    app.run()
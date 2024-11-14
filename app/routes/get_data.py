from flask import Flask, request, jsonify
from app.service.producers_service.all_messages_producer import publish_message

app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def receive_email():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    success = publish_message(data)
    return jsonify({
        "status": f"Message received {success} rows",
    }), 200


if __name__ == '__main__':
    app.run()
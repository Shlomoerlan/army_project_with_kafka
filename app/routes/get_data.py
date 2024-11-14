from flask import Flask, request, jsonify
from app.utils.selector import check_if_contains_suspicious_content

app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def receive_email():
    data = request.json
    print("email router", data)
    check_if_contains_suspicious_content(data)
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    return jsonify({
        "status": f"Message received",
    }), 200





if __name__ == '__main__':
    app.run()
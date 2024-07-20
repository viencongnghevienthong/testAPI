from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    # Xử lý dữ liệu ở đây
    print("Received data:", data)
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run()

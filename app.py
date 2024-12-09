from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status": "Bot actif", "uptime": "3h20m"})

if __name__ == '__main__':
    app.run(debug=True)

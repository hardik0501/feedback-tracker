from flask import Flask, request, jsonify
from utils.feedback_store import store_feedback, get_all_feedback, get_summary

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Real-Time Feedback Tracker"})

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    store_feedback(data)
    return jsonify({"message": "Feedback received"}), 201

@app.route('/feedback', methods=['GET'])
def show_feedback():
    return jsonify(get_all_feedback())

@app.route('/summary', methods=['GET'])
def summary():
    return jsonify(get_summary())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

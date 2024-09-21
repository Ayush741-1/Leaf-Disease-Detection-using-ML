from flask import Flask, request, jsonify, send_from_directory
from predict_leaf_disease import predict_disease
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        try:
            prediction = predict_disease(file)
            return jsonify({'prediction': prediction}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

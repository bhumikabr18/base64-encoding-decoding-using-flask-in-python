# Flask application for Base64 encoding/decoding
# Loom video for demo: https://www.loom.com/share/387125355a984f49bfb3317aad69c582?sid=60dfe16a-e57c-410c-a31a-1a17a9ea94b3
from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Function to encode input to Base64
def encode_base64(data):
    # Convert string to bytes, then encode in base64
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return encoded_data

# Function to decode Base64 input
def decode_base64(data):
    # Decode base64 string, then convert bytes to string
    decoded_data = base64.b64decode(data.encode('utf-8')).decode('utf-8')
    return decoded_data

# Route to encode input
@app.route('/encode', methods=['POST'])
def encode():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No input provided'}), 400
    try:
        # Convert the input to string
        encoded_data = encode_base64(str(data))
        return jsonify({'encoded': encoded_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to decode input
@app.route('/decode', methods=['POST'])
def decode():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No input provided'}), 400
    try:
        # Convert the input to string
        decoded_data = decode_base64(str(data))
        return jsonify({'decoded': decoded_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

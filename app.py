from flask import Flask, request, jsonify
from geopy.distance import geodesic
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
CORS(app)

@app.route('/check_proximity', methods=['POST'])
def check_proximity():
    try:
        data = request.get_json()
        print("Received data:", data, file=sys.stderr)  # Debug log

        if not data:
            return jsonify({'error': 'No JSON provided'}), 400

        warehouse_coords = tuple(data.get('warehouse', []))
        delivery_coords = tuple(data.get('delivery', []))
        radius_raw = data.get('radius', 250)

        # Validate coordinates
        if len(warehouse_coords) != 2 or len(delivery_coords) != 2:
            return jsonify({'error': 'Invalid coordinates'}), 400

        # Ensure radius is a number
        try:
            radius = float(radius_raw)
        except (TypeError, ValueError):
            return jsonify({'error': 'Radius must be a number'}), 400

        distance = geodesic(warehouse_coords, delivery_coords).meters
        is_within_range = distance <= radius

        return jsonify({
            'distance': round(distance, 2),
            'within_range': is_within_range
        })
    except Exception as e:
        print("Error:", str(e), file=sys.stderr)
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, request, jsonify
import os
from google.cloud import storage
from google.oauth2 import service_account
import base64
import json
import uuid

app = Flask(__name__)

# Load GCP credentials from environment variable
sa_key = os.getenv('RS_GCP_SA_KEY')
if sa_key:
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(base64.b64decode(sa_key).decode('utf-8'))
    )
else:
    raise ValueError("No service account key provided")

# Initialize GCP Storage client
client = storage.Client(credentials=credentials)
bucket_name = "rs-gcp-flask"  
bucket = client.bucket(bucket_name)

# Helper functions
def save_to_gcp(record, record_id):
    blob = bucket.blob(record_id)
    blob.upload_from_string(json.dumps(record))

def read_from_gcp(record_id):
    blob = bucket.blob(record_id)
    if not blob.exists():
        return None
    return json.loads(blob.download_as_string())

# CRUD operations
@app.route('/record', methods=['POST'])
def create_record():
    data = request.json
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid data"}), 400

    record_id = str(uuid.uuid4())
    save_to_gcp(data, record_id)
    return jsonify({"id": record_id}), 201

@app.route('/record/<record_id>', methods=['GET'])
def read_record(record_id):
    record = read_from_gcp(record_id)
    if record is None:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record), 200

@app.route('/record/<record_id>', methods=['PUT'])
def update_record(record_id):
    data = request.json
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    existing_record = read_from_gcp(record_id)
    if existing_record is None:
        return jsonify({"error": "Record not found"}), 404

    save_to_gcp(data, record_id)
    return jsonify({"message": "Record updated"}), 200

@app.route('/record/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    blob = bucket.blob(record_id)
    if not blob.exists():
        return jsonify({"error": "Record not found"}), 404

    blob.delete()
    return jsonify({"message": "Record deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

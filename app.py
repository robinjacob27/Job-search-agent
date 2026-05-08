from flask import Flask, jsonify, request
from datetime import datetime
import json
import os

app = Flask(__name__)

# Store applications in a simple JSON file
APPLICATIONS_FILE = 'applications.json'

def load_applications():
    if os.path.exists(APPLICATIONS_FILE):
        with open(APPLICATIONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_applications(apps):
    with open(APPLICATIONS_FILE, 'w') as f:
        json.dump(apps, f, indent=2)

@app.route('/api/apply', methods=['POST'])
def submit_application():
    """Submit an auto-application to a job"""
    data = request.json
    
    app_data = {
        'id': data.get('job_id'),
        'title': data.get('title'),
        'company': data.get('company'),
        'applied_at': datetime.now().isoformat(),
        'status': 'submitted',
        'apply_url': data.get('apply_url')
    }
    
    applications = load_applications()
    applications.append(app_data)
    save_applications(applications)
    
    return jsonify({
        'success': True,
        'message': f"Successfully applied to {data.get('title')} at {data.get('company')}",
        'application': app_data
    }), 200

@app.route('/api/applications', methods=['GET'])
def get_applications():
    """Get all submitted applications"""
    applications = load_applications()
    return jsonify(applications), 200

@app.route('/api/applications/<job_id>', methods=['DELETE'])
def remove_application(job_id):
    """Remove an application record"""
    applications = load_applications()
    applications = [a for a in applications if a['id'] != job_id]
    save_applications(applications)
    return jsonify({'success': True}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

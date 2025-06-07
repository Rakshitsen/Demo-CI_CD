from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'message': 'Flask app is running successfully!'
    })

@app.route('/api/info')
def app_info():
    return jsonify({
        'app': 'Flask CI/CD Demo',
        'version': '1.0.0',
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'build_id': os.environ.get('CODEBUILD_BUILD_ID', 'local')
    })

@app.route('/api/users')
def get_users():
    # Dummy users data
    users = [
        {'id': 1, 'name': 'Rahul', 'email': 'rahul@example.com'},
        {'id': 2, 'name': 'Priya', 'email': 'priya@example.com'},
        {'id': 3, 'name': 'Amit', 'email': 'amit@example.com'}
    ]
    return jsonify(users)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

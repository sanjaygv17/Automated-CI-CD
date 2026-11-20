from flask import Blueprint, jsonify,render_template
from datetime import datetime, timezone
import os
import platform

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@main.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@main.route('/api/info', methods=['GET'])
def application_info():
    return jsonify({
        "project": "Python CI/CD Pipeline",
        "backend": "Flask",
        "containerization": "Docker",
        "automation": "GitHub Actions",
        "image_registry": "Docker Hub",
        "deployment": "Render",
        "version": "2.0.0"
    })


@main.route('/api/status', methods=['GET'])
def system_status():
    return jsonify({
        "application_status": "running",
        "python_version": platform.python_version(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "server_time": datetime.now(timezone.utc).isoformat()
    })


@main.route('/api/version', methods=['GET'])
def version():
    return jsonify({
        "version": "2.0.0",
        "release": "Initial DevOps deployment"
    })
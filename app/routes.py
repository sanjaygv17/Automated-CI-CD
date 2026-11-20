from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Python CI Project",
        "status": "success"
    })

@main.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy"
    })


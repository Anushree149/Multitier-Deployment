# backend/app.py
from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'example'),
    'host': os.getenv('DB_HOST', 'db'),
    'database': os.getenv('DB_NAME', 'app_db')
}

@app.route('/')
def index():
    return jsonify(message="Welcome to the Flask backend!")

@app.route('/data')
def get_data():
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, Docker Swarm!' AS message;")
    result = cursor.fetchone()
    connection.close()
    return jsonify(message=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

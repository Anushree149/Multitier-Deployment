# backend/app.py
from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Database configuration
db_config = {
    'dbname': os.getenv('DB_NAME', 'app_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'example'),
    'host': os.getenv('DB_HOST', 'db')
}

@app.route('/')
def index():
    return jsonify(message="Welcome to the Flask backend!")

@app.route('/data')
def get_data():
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, Docker Swarm with PostgreSQL!' AS message;")
    result = cursor.fetchone()
    connection.close()
    return jsonify(message=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

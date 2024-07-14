# app.py

import logging
import json
from flask import Flask, render_template, request, jsonify
from logging_config import log_json  # Импортируйте вашу функцию логирования

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Пример использования функции логирования
data = {"key": "value"}
log_json(data)

# Настройка приложения Flask
app = Flask(__name__)

# Пример данных для тестирования
endpoints = {
    "Test Endpoint 1": "https://jsonplaceholder.typicode.com/posts/1",
    "Test Endpoint 2": "https://jsonplaceholder.typicode.com/posts/2"
}

params = {
    "Param 1": "1",
    "Param 2": "2"
}


@app.route('/')
def index():
    return render_template('index.html', endpoints=endpoints, params=params)


@app.route('/call_endpoints', methods=['POST'])
def call_endpoints():
    data = request.json
    endpoints = data.get('endpoints', [])

    responses = {}
    for endpoint_data in endpoints:
        try:
            endpoint = endpoint_data['endpoint']
            param = endpoint_data['param']
            response = requests.get(f"{endpoint}?param={param}")
            response_json = response.json()
            responses[endpoint] = response_json
            log_json(response_json)  # Логирование JSON ответа
        except Exception as e:
            logging.error(f'Error calling endpoint {endpoint}: {e}')
            responses[endpoint] = {"error": str(e)}

    return jsonify(responses)


if __name__ == "__main__":
    app.run(debug=True)

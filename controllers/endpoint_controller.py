# controllers/endpoint_controller.py

import requests
from logging_config import log_json


class EndpointController:
    def __init__(self, endpoints):
        self.endpoints = endpoints

    def call_endpoints(self, endpoints):
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
        return responses

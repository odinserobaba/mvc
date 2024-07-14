import requests
import logging


class EndpointCaller:
    def __init__(self, endpoints):
        self.endpoints = endpoints

    def call_endpoints(self):
        for endpoint in self.endpoints:
            response = requests.get(endpoint)
            logging.info(
                f"Called {endpoint}, response: {response.status_code}")

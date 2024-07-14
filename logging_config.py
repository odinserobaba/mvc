# logging_config.py

import logging
import json

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Пример логирования JSON


def log_json(data):
    logging.info(f'JSON Data: {json.dumps(data, indent=2)}')

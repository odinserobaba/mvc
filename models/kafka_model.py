from kafka import KafkaConsumer
import logging


class KafkaMessageProcessor:
    def __init__(self, brokers, topic):
        self.consumer = KafkaConsumer(topic, bootstrap_servers=brokers)

    def process_messages(self):
        for message in self.consumer:
            logging.info(f"Received message: {message.value}")
            # Обработка сообщения

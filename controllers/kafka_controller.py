from kafka import KafkaConsumer
import logging


class KafkaController:
    def __init__(self, ssh_host, ssh_user, ssh_key_path, topic):
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.ssh_key_path = ssh_key_path
        self.topic = topic

    def process_messages(self):
        try:
            consumer = KafkaConsumer(
                self.topic, bootstrap_servers=[self.ssh_host])
            for message in consumer:
                logging.info(
                    f'Received message from Kafka topic {self.topic}: {message.value.decode()}')
                # Добавьте логику обработки сообщений здесь
            logging.info('Processed Kafka messages successfully.')
        except Exception as e:
            logging.error(f'Error processing Kafka messages: {e}')
            raise

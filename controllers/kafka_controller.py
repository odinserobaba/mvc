from models.kafka_model import KafkaMessageProcessor


class KafkaController:
    def __init__(self, brokers, topic):
        self.processor = KafkaMessageProcessor(brokers, topic)

    def process_messages(self):
        self.processor.process_messages()

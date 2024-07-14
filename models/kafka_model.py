class KafkaMessageProcessor:
    def __init__(self, ssh_host, ssh_user, ssh_key_path, topic):
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.ssh_key_path = ssh_key_path
        self.topic = topic

    def process_messages(self):
        print(f"Simulating message processing for topic: {self.topic}")
        # Simulate message processing

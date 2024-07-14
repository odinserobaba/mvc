class LogCollector:
    def __init__(self, ssh_host, ssh_user, ssh_key_path, namespace='default'):
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.ssh_key_path = ssh_key_path
        self.namespace = namespace

    def collect_logs(self):
        print(f"Simulating log collection for namespace: {self.namespace}")
        with open('logs/dummy.log', 'w') as log_file:
            log_file.write("Dummy log data")

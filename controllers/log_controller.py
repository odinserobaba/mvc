from models.log_model.py import LogCollector


class LogController:
    def __init__(self, namespace='default'):
        self.collector = LogCollector(namespace)

    def collect_logs(self):
        self.collector.collect_logs()

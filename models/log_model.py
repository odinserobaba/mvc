from kubernetes import client, config

class LogCollector:
    def __init__(self, namespace='default'):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()
        self.namespace = namespace

    def collect_logs(self):
        pods = self.v1.list_namespaced_pod(self.namespace)
        for pod in pods.items:
            name = pod.metadata.name
            logs = self.v1.read_namespaced_pod_log(name, self.namespace)
            with open(f'logs/{name}.log', 'w') as log_file:
                log_file.write(logs)

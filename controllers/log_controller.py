import paramiko
import logging


class LogController:
    def __init__(self, ssh_host, ssh_user, ssh_key_path, namespace):
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.ssh_key_path = ssh_key_path
        self.namespace = namespace

    def collect_logs(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.load_system_host_keys()
            ssh.connect(self.ssh_host, username=self.ssh_user,
                        key_filename=self.ssh_key_path)
            stdin, stdout, stderr = ssh.exec_command(
                f"kubectl logs -n {self.namespace}")
            logs = stdout.read().decode('utf-8')
            ssh.close()
            logging.info(f'Collected logs from namespace {self.namespace}.')
            return logs
        except Exception as e:
            logging.error(f'Error collecting logs: {e}')
            raise

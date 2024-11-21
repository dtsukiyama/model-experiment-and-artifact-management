import os
import json
import datetime


class ExperimentLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

    def log_metrics(self, run_id, metrics):
        """
        Logs metrics to a JSON file.
        :param run_id: Unique identifier for the experiment run.
        :param metrics: Dictionary of metrics to log.
        """
        log_file = os.path.join(self.log_dir, f"{run_id}_metrics.json")
        with open(log_file, "w") as f:
            json.dump(metrics, f)

    def log_params(self, run_id, params):
        """
        Logs parameters to a JSON file.
        :param run_id: Unique identifier for the experiment run.
        :param params: Dictionary of parameters to log.
        """
        log_file = os.path.join(self.log_dir, f"{run_id}_params.json")
        with open(log_file, "w") as f:
            json.dump(params, f)

    def log_message(self, run_id, message):
        """
        Logs a plain text message.
        :param run_id: Unique identifier for the experiment run.
        :param message: Message to log.
        """
        log_file = os.path.join(self.log_dir, f"{run_id}_log.txt")
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")

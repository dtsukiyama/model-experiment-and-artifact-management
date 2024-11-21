import mlflow


class MLflowLogger:
    def __init__(self, experiment_name="default_experiment", tracking_uri=None):
        """
        Initializes MLflow and sets the experiment.
        :param experiment_name: Name of the MLflow experiment.
        :param tracking_uri: URI for the MLflow tracking server.
        """
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)

        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)

    def start_run(self, run_name=None):
        """
        Starts an MLflow run.
        :param run_name: Optional name for the run.
        """
        self.run = mlflow.start_run(run_name=run_name)
        return self.run.info.run_id

    def log_params(self, params):
        """
        Logs parameters to the current MLflow run.
        :param params: Dictionary of parameters.
        """
        for key, value in params.items():
            mlflow.log_param(key, value)

    def log_metrics(self, metrics):
        """
        Logs metrics to the current MLflow run.
        :param metrics: Dictionary of metrics.
        """
        for key, value in metrics.items():
            mlflow.log_metric(key, value)

    def log_artifact(self, file_path):
        """
        Logs an artifact to the current MLflow run.
        :param file_path: Path to the artifact file.
        """
        mlflow.log_artifact(file_path)

    def end_run(self):
        """
        Ends the current MLflow run.
        """
        mlflow.end_run()

import os
from experiment_tracking.mlflow_integration import MLflowLogger


def test_mlflow_logger():
    # Initialize MLflow logger
    mlflow_logger = MLflowLogger(experiment_name="Test Experiment")

    # Start a run
    run_id = mlflow_logger.start_run(run_name="test_run")
    assert run_id is not None

    # Log parameters and metrics
    mlflow_logger.log_params({"param1": 10})
    mlflow_logger.log_metrics({"metric1": 0.99})

    # Log a dummy artifact
    with open("test_artifact.txt", "w") as f:
        f.write("Dummy artifact")
    mlflow_logger.log_artifact("test_artifact.txt")
    os.remove("test_artifact.txt")

    # End the run
    mlflow_logger.end_run()

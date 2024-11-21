import os
from experiment_tracking.logger import ExperimentLogger

def test_logger():
    logger = ExperimentLogger(log_dir="test_logs")
    run_id = "test_run"
    logger.log_params(run_id, {"param1": 10})
    logger.log_metrics(run_id, {"metric1": 0.99})
    logger.log_message(run_id, "Test message")

    assert os.path.exists(f"test_logs/{run_id}_params.json")
    assert os.path.exists(f"test_logs/{run_id}_metrics.json")
    assert os.path.exists(f"test_logs/{run_id}_log.txt")

import os
import shutil
import boto3


class ArtifactManager:
    def __init__(self, local_dir="artifacts", s3_bucket=None):
        self.local_dir = local_dir
        self.s3_bucket = s3_bucket
        os.makedirs(local_dir, exist_ok=True)
        self.s3_client = boto3.client("s3") if s3_bucket else None

    def save_artifact(self, artifact_name, content):
        """
        Saves an artifact locally.
        :param artifact_name: Name of the artifact file.
        :param content: Content to save.
        """
        artifact_path = os.path.join(self.local_dir, artifact_name)
        with open(artifact_path, "w") as f:
            f.write(content)

    def upload_to_s3(self, artifact_name):
        """
        Uploads an artifact to S3.
        :param artifact_name: Name of the artifact file.
        """
        if not self.s3_client:
            raise ValueError("S3 bucket is not configured.")

        artifact_path = os.path.join(self.local_dir, artifact_name)
        self.s3_client.upload_file(artifact_path, self.s3_bucket, artifact_name)

    def clean_local(self):
        """Cleans up local artifacts."""
        shutil.rmtree(self.local_dir)
        os.makedirs(self.local_dir, exist_ok=True)

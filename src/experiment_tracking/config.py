import yaml


class ConfigManager:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """
        Loads the configuration file.
        """
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def get(self, key, default=None):
        """
        Gets a configuration value.
        :param key: Key to retrieve.
        :param default: Default value if key is not found.
        """
        return self.config.get(key, default)

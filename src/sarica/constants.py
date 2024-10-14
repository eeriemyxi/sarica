import yaml

CONFIG = "config.yaml"
with open(CONFIG) as config_buf:
    config = yaml.safe_load(config_buf)

EMAIL = config["EMAIL"]
PASSWORD = config["PASSWORD"]
SEED = None

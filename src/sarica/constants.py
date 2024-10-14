import yaml
import pathlib
import sys
import os

if sys.platform != "linux":
    raise RuntimeError("Your platform is not supported.")

IS_ANDROID = hasattr(sys, "getandroidapilevel")

CONFIG = pathlib.Path(os.environ["HOME"])/ ".config" / "sarica" / "config.yaml"
with open(CONFIG) as config_buf:
    config = yaml.safe_load(config_buf)

EMAIL = config["EMAIL"]
PASSWORD = config["PASSWORD"]
SEED = None

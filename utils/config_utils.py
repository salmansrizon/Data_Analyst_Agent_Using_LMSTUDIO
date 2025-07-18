import yaml
from pathlib import Path


def load_config():
    config_path = Path(__file__).parent.parent / "config/agent.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


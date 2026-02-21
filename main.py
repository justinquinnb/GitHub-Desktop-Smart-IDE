import subprocess
import sys
from pathlib import Path
import yaml

def open_preferred_launcher():
    target_path = sys.argv[1]
    jqb_config = Path(target_path).joinpath(".jqb-devtools/config.yaml")

    with open(jqb_config, "r") as config_file:
        config_data = yaml.safe_load(config_file)

    ide_executable = config_data["default_ide_executable"]
    subprocess.run([ide_executable, target_path])

if __name__ == "__main__":
    open_preferred_launcher()

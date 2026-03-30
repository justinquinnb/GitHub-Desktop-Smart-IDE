import subprocess
import sys
from pathlib import Path
import yaml

def open_preferred_launcher():
    target_path = sys.argv[1]
    jqb_config = Path(target_path).joinpath(".jqb-devtools/config.yaml")

    with open(jqb_config, "r") as config_file:
        config_data = yaml.safe_load(config_file)

    try:
        ide_executable = config_data["preferred-ide"]
        subprocess.run([ide_executable, target_path])
    except KeyError:
        print("ERROR: No preferred IDE configured.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    open_preferred_launcher()

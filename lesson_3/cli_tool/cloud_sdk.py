import time
import random
from .utils import dict_to_str
from .validation import DeployException


def fake_deploy(options):
    print(f"Deploying with options: {dict_to_str(options)}")
    for _ in range(7):
        if random.randrange(1, 100) > 90:
            raise DeployException("failed deployment")
        print(".", end="", flush=True)
        time.sleep(1)
    print("\nDeployment Done. :)")


def fake_restart(options):
    print(f"Restart options: {dict_to_str(options)}")

    if "service" in options and options["service"] in ["backend", "frontend"]:
        print("\nRestarted service")
        return
    raise Exception("Failed to restart service")

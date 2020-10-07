import time
import random
from .utils import dict_to_str
from .validation import DeployException


def fake_deploy(options):
    options.update({"service": "backend"})
    print(f"Deploying with options: {dict_to_str(options)}")
    for _ in range(7):
        if random.randrange(1, 100) > 90:
            raise DeployException("failed deployment")
        print(".", end="", flush=True)
        time.sleep(1)
    print("\nDeployment Done. :)")

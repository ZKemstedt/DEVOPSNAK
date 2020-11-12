import time
import random

from .utils import dict_to_str
from .validation import DeployException

""" THIS FILE IS THE PROPERTY OF RANDOM A3D CLOUD INC.
    MODIFICATION OF THIS FILE IS STRICTLY FORBIDDEN

    DON'T WRITE ANY TESTS, the code is already of highest possible quality.
"""


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

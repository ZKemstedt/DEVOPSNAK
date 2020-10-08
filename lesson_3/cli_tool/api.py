from .validation import validate_deploy_options, DeployException
from .cloud_sdk import fake_deploy


def deploy(**kwargs):
    options = {
        "conf": "test",
        "timeout": "1m"
    }
    options.update(kwargs)
    validate_deploy_options(options)

    try:
        fake_deploy(options)
    except DeployException as df:
        print(df)
        return 255
    return False

from .validation import validate_deploy_options, DeployException
from .cloud_sdk import fake_deploy, fake_restart


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


def restart(**kwargs):
    options = {}  # extendable with default arguments
    options.update(kwargs)
    try:
        fake_restart(options)
    except Exception as e:
        print(e)
        return 255
    return False

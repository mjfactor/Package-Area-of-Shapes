# version.py
import subprocess


def get_latest_tag():
    try:
        latest_tag = subprocess.check_output(["git", "describe", "--tags"]).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        latest_tag = None
    return latest_tag


version = get_latest_tag().split('-')[0]
print(version)

__version__ = '3.4'

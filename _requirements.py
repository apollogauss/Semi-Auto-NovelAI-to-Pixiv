import os
import shutil
import subprocess
import sys

requirements_checked = False


def install_requirements():
    global requirements_checked
    if requirements_checked:
        return
    requirements_checked = True
    print('Detected missing dependencies, installing requirements...')
    subprocess.call(f"{sys.executable} -s -m pip install -r requirements.txt")


try:
    from utils.env import env
except ModuleNotFoundError:
    install_requirements()
    from utils.env import env

try:
    os.remove('main.py')
except FileNotFoundError:
    pass

if env.new_interface:
    shutil.copyfile('./files/webui/main_new.py', 'main.py')
else:
    shutil.copyfile('./files/webui/main_bak.py', 'main.py')


try:
    import main  # noqa
    from files.SANP_DOCS import launch  # noqa
    from src import *  # noqa
    from utils import *  # noqa
except ModuleNotFoundError:
    install_requirements()

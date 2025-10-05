import os
import subprocess
import sys

from utils.prepare import logger


def restart():
    logger.warning("开始重启...")
    python = sys.executable
    args = [python, *sys.argv]
    subprocess.Popen(args, cwd=os.getcwd())
    os._exit(0)

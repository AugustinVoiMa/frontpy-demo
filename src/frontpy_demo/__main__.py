import sys
from os.path import dirname, join

from frontpy_core.app import App

__APP_DIR__ = dirname(__file__)

sys.path.append(join(__APP_DIR__, 'src'))
App(__APP_DIR__).launch()

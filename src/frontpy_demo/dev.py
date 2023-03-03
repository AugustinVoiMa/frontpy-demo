from os.path import dirname

from frontpy_core.dev_worker import launch_dev_worker

if __name__ == '__main__':
    launch_dev_worker(dirname(__file__))

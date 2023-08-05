"""# Entrypoint
"""
from .app import LiteraryApp, launch_new_instance
if __name__ == '__main__' and (not LiteraryApp.initialized()):
    launch_new_instance()
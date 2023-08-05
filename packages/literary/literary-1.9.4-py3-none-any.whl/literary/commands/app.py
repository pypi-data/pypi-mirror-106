"""# Commandline Application
"""
import sys
from jupyter_core.application import JupyterApp
from traitlets import default
from . import build, test
from ..core.config import CONFIG_FILE_NAME

class LiteraryApp(JupyterApp):
    name = 'literary'
    description = 'Work with literate notebooks'
    subcommands = {'build': (build.LiteraryBuildApp, 'Build a package from a series of notebooks'), 'test': (test.LiteraryTestApp, 'Run a series of notebook tests')}

    @default('config_file_name')
    def config_file_name_default(self):
        return CONFIG_FILE_NAME

    def start(self):
        """Perform the App's actions as configured"""
        super().start()
        sub_commands = ', '.join(sorted(self.subcommands))
        sys.exit('Please supply at least one subcommand: {}'.format(sub_commands))
launch_new_instance = LiteraryApp.launch_instance
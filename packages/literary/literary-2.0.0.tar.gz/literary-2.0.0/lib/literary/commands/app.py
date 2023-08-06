
"""# Literary Application
"""
from copy import deepcopy
from pathlib import Path
from traitlets import Unicode, default
from traitlets.config import Application, catch_config_error
from ..core.project import ProjectOperator
from ..core.trait import Path as PathTrait
from ..core.config import find_project_config, load_project_config

class LiteraryApp(Application):
    name = 'literary'
    description = 'A Literary application'
    aliases = {'config-file': 'LiteraryApp.project_config_file'}
    project_config_file = PathTrait(help='Literary project configuration file').tag(config=True)

    @default('project_config_file')
    def _project_config_file_default(self):
        return find_project_config(Path.cwd())

    @catch_config_error
    def initialize(self, argv=None):
        self.parse_command_line(argv)
        argv_config = deepcopy(self.config)
        self.load_app_config_file()
        self.update_config(argv_config)

    def load_app_config_file(self):
        config = load_project_config(self.project_config_file)
        self.update_config(config)

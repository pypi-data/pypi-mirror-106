"""# Notebook helper namespace
"""
import pathlib
import sys
from ..core import config
from . import importer
from .patch import patch
_PACKAGE_ROOT_PATH = config.find_project_path()

def _update_namespace(namespace):
    """Update a namespace with the missing metadata required to support runtime
    imports of notebooks

    :param namespace: namespace object
    :return:
    """
    namespace['__package__'] = importer.determine_package_name(pathlib.Path.cwd(), _PACKAGE_ROOT_PATH)
    namespace['patch'] = patch

def load_ipython_extension(ipython):
    """Load the import hook and setup the global state for the Literary extension.
    When IPython invokes this function, the determined package root path will be
    added to `sys.path`.

    :param ipython: IPython shell instance
    """
    _update_namespace(ipython.user_ns)
    importer.install_hook(_PACKAGE_ROOT_PATH)
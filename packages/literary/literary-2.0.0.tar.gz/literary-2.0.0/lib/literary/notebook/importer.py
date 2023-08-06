
"""# Import Hook
"""
import os
import sys
import typing as tp
from pathlib import Path
from nbconvert import Exporter
from traitlets import Bool, Instance, Type
from ..core.exporter import LiteraryExporter
from ..core.project import ProjectOperator
from .finder import inject_loaders
from .loader import NotebookLoader
from .patch import patch

class ProjectImporter(ProjectOperator):
    exporter = Instance(Exporter)
    exporter_class = Type(LiteraryExporter, help='Exporter class').tag(config=True)
    set_except_hook = Bool(help='overwrite `sys.excepthook` to correctly display tracebacks').tag(config=True)

    def determine_package_name(self, path: Path) -> str:
        """Determine the corresponding importable name for a package directory given by
    a particular file path. Return `None` if path is not contained within `sys.path`.

    :param path: path to package
    :return:
    """
        for p in sys.path:
            if (str(path) == p):
                continue
            try:
                relative_path = path.relative_to(p)
            except ValueError:
                continue
            return '.'.join(relative_path.parts)
        return None

    def install(self, ipython):
        """Install notebook import hook

    Don't allow the user to specify a custom search path, because we also need this to
    interoperate with the default Python module importers which use sys.path

    :return:
    """
        sys.path.append(str(self.packages_path))
        exporter = self.exporter_class(parent=self)

        def create_notebook_loader(fullname, path):
            return NotebookLoader(fullname, path, exporter=exporter)
        inject_loaders(sys.path_hooks, (create_notebook_loader, ['.ipynb']))
        if self.set_except_hook:
            sys.excepthook = traceback.print_exception
        ipython.user_ns.update({'__package__': self.determine_package_name(Path.cwd()), 'patch': patch})

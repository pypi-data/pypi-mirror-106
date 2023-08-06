#!/usr/bin/env python3

import autocleus.library.venv_utils as virtenv
from pydantic import BaseModel, SecretStr, BaseSettings, Extra
from typing import Dict, Any, Union, Type, List, Optional
import contextlib
import os



@contextlib.contextmanager
def working_dir(directory=None):
    """Context manager version of os.chdir.
    When exited, returns to the working directory prior to entering.
    """
    cwd = os.getcwd()
    try:
        if directory is not None:
            os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)

class BaseHook(BaseModel):
    """Base hook mixin class."""

    chdir: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        extra = Extra.forbid
        # orm_mode = True

    def execute(self) -> Any:
        """Abstract method."""
        raise NotImplementedError()

    def call(self) -> Any:
        """
        Call main entrypoint to calling hook.
        Handles `chdir` method.
        """
        if self.chdir and os.path.isdir(
            os.path.abspath(os.path.expanduser(self.chdir))
        ):
            # Use contextlib to switch dirs and come back out
            with working_dir(os.path.abspath(os.path.expanduser(self.chdir))):
                return self.execute()
        elif self.chdir and not os.path.exists(self.chdir):
            os.mkdir(self.env_root)
            os.chmod(self.env_root, 0o755)

            with working_dir(os.path.abspath(os.path.expanduser(self.chdir))):
                return self.execute()
        else:
            return self.execute()
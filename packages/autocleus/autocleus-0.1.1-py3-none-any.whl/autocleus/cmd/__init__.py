#!/usr/bin/env python3

import sys
#from loguru import logger

SETUP_PARSER = 'setup_parser'


def cmd_name(python_name):
    """Convert module name (with ``_``) to command name (with ``-``)."""
    return python_name.replace('_', '-')

def python_name(cmd_name):
    """Convert ``-`` to ``_`` in command name, to make a valid identifier."""
    return cmd_name.replace("-", "_")


def get_module(cmd_name, modpath=__name__, mod=SETUP_PARSER):
    """
    Imports the module for a porticular command name and returns it
    
    Args:
        cmd_name (str): name of the command for which to get the module
              (python modules contain ``_``, not ``-`` like spack commands do)

        from_list_ (list [str]): list of functions to import from top level class

    Adapted from spack.cmd
    """
    pname = python_name(cmd_name)

    try:
        # Try to import the command from the built-in directory
        module_name = "{}.{}".format(modpath, pname)
        module = __import__(module_name,
                            fromlist=[pname, mod],
                            level=0)
    except Exception as err:
        print(err)
        #logger.exception("{} | No module found for command: {} |".format(err, cmd_name))
        return False 
    
    return module


def get_command(cmd_name, modpath=__name__, mod=SETUP_PARSER):
    """Imports the command function associated with cmd_name.
    The function's name is derived from cmd_name using python_name().
    Args:
        cmd_name (str): name of the command (contains ``-``, not ``_``).
    """

    pname = python_name(cmd_name)
    return getattr(get_module(cmd_name, modpath=modpath, mod=mod), pname)


#: global, cached list of all commands -- access through all_commands()
_all_commands = None

def all_commands():
    """
    Get a sorted list of all commands.
    This will list the cmd directory and find the
    commands there to construct the list.  It does not actually import
    the python files -- just gets the names.
    """
    global _all_commands
    if _all_commands is None:
        _all_commands = []
        command_paths = [monTransfer.paths.command_path]  # Built-in commands
        for path in command_paths:
            for file in os.listdir(path):
                if file.endswith(".py") and not re.search(ignore_files, file):
                    cmd = re.sub(r'.py$', '', file)
                    _all_commands.append(cmd_name(cmd))

        _all_commands.sort()

    return _all_commands

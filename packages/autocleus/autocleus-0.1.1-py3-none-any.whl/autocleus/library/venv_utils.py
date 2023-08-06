#!/usr/bin/env python3

import os
import sys
import venv
from pip._internal import main as pipmain 
from pip._internal.utils.misc import get_installed_distributions
import subprocess


def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix


def in_virtualenv_currently():
    """Check whether currently running inside of a virtualenv or not"""
    return get_base_prefix_compat() != sys.prefix


def create_virtualenv(env_root, permissions=0o755):
    """
    Create a python virtual environment in a specified directory

    Args:
        env_root(str): absolute path to directory where virtual environment
        should be created. The env_root directory will serve as the custom
        cli's root directory. It should be a subdirectory in the directory 
        entered  by user as the project directory. (<userdir>/cli_name/cli_name)

        permissions(char): linux directory permission. Python syntax does not
        allow numbers starting with 0, must be written 0oXXX (Python 3)
    """

    if not os.path.exists(env_root):
        # create base directory for virtual env
        os.mkdir(env_root, permissions)

    if not in_virtualenv_currently():
        try:
            venv.create(env_root, with_pip=True)
        except Exception as e:
            print(f"Unable to to create virtualvenv due to following exception {e}")


def venv_mock_activate(env_root):

    # set virtualenv environment variable to venv root dir
    os.environ['VIRTUAL_ENV'] = env_root
    
    # unset pythonhome if set but store old path for mock deactivate
    if os.environ.get('PYTHONHOME'):
        os.environ['_OLD_PYTHONHOME'] = os.environ['PYTHONHOME']
        os.environ['PYTHONHOME'] = ''
    
    # prepend virtualenv bin to PATH
    os.environ['PATH'] = f"{env_root}/bin" + os.pathsep + os.environ['PATH']


def venv_mock_deactivate(env_root):

    # unset virtualenv environment variable
    del os.environ['VIRTUAL_ENV']

    # reset original pythonhome if it was set
    if os.environ.get('_OLD_PYTHONHOME'):
        os.environ['PYTHONHOME'] = os.environ['_OLD_PYTHONHOME']
        del os.environ['_OLD_PYTHONHOME']
    
    # remove virtualenv bin from PATH
    new_paths = [x for x in list(os.environ['PATH'].split(os.pathsep))
                if env_root not in x]
    os.environ['PATH'] = os.pathsep.join(new_paths)


def install_packages_to_venv(env_root, pkg_list):
    for pkg in pkg_list:
        #pipmain(['install',  pkg])
        subprocess.call([f"{env_root}/bin/pip3", "install", "-q", f"{pkg}"])



def list_venv_installed_packages():
    """Lists all packages installed in venv"""
    distributions = get_installed_distributions()

    pkgs = {}

    for dist in distributions:
        pkgs[dist.__dict__['project_name']] = dist.__dict__['_version']

    return pkgs


def output_project_requirements(env_root, pkgs=None):
    

    if not pkgs:
        pkgs = list_venv_installed_packages()

        with open(f'{env_root}/requirements.txt', 'wb') as reqs:
            for pkg_name, version in pkgs.items():
                reqs.writelines(f'{pkg_name}=={version}')
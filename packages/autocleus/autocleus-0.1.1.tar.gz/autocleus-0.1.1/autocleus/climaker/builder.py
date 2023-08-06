#!/usr/bin/env python3

# clean up imports
from setuptools import sandbox
# how to propertly import DirectorySandbox
from setuptools.command.easy_install import chmod, current_umask
from setuptools.sandbox import DirectorySandbox
#from setuptools import sandbox.DirectorySandbox as DirectorySandbox
import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape, StrictUndefined
import autocleus.cmd as cmd
import distutils.cmd
import setuptools
from autocleus.library import classproperty
from distutils.core import setup, Command

    

def _execfile(template, globals=dict(__file__='setup.py', 
            __name__='__main__'), filename='setup.py', 
            locals=None):
    """
    Adaptation of execfile for rendered jinja template

    Args:
        template(str): rendered jinja2 template for setup.py
        globals(dict): methods that should be globally accesible
        filename(str): name of file from which script was loaded (
            if not read from string, just use any name but should
            matcht __file__ in globals)
        locals(str): mapping object
    """
    if locals is None:
        locals = globals
    # use sys.argv to set cutom arguments --cli-name=mycli
    code = compile(template, filename, 'exec')
    exec(code, globals, locals)


def get_script(script):
    """
    Return base script class
    """
    return cmd.get_module('builder', modpath='climaker.builder', mod=f'{script}Script')

class VirtualScriptClass(type):
    '''
    MetaClass for VirtualScript classes
    '''

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class VirtualScript(object):
    """
    Base Virtual Script File

    # Adapated from PyPi license
    """

    __metaclass__ = VirtualScriptClass

    jinja_env = Environment(loader=PackageLoader('autocleus', 'templates'),
                            autoescape=['.j2'],
                            undefined=StrictUndefined,
                            trim_blocks=True,
                            lstrip_blocks=True
                            )

    def __init__(self):
        raise TypeError('VirtualScript classes are not being initiated')

    @classproperty
    def name(cls):
        name = cls.__doc__
        if not name:
            raise AttributeError('{} has no docstring'.format(cls.__name__))
        return name.strip()

    @classmethod
    def _check(cls):
        if cls == VirtualScript:
            raise TypeError('This is a virtual class, do not call it\'s methods')
    
    @classmethod
    def execute(cls, **kwargs):
        if cls.cmd_line_args :
            # local_vars is expected to be dict
            local_vars = cls.cmd_line_args
        else:
            local_vars = None
        
        try:
            with DirectorySandbox(cls.path):
                setup_script = cls.render(**kwargs)
                _execfile(setup_script, locals=local_vars)
        
        except SystemExit as v:
            if v.args and v.args[0]:
                raise
            # Normal exit, just return

    @classmethod
    def render(cls, **kwargs):
        """
        Render the Python code object file
        """
        cls._check()
        template = cls.jinja_env.get_template(cls.id)
        return template.render(**kwargs)
    
    @classmethod
    def write(cls, **kwargs):
        """
        Write python code object to file
        """
        mask = current_umask()
        script = cls.render(**kwargs)
        target = os.path.join(cls.path, cls.filename)
        
        with open(f"{target}", 'w') as out:
            out.write(script)
        chmod(target, cls.permissions - mask)        
        
    
class SetupScript(VirtualScript):
    """
    Basic setup.py script
    """
    id = 'setup'
    filename = 'setup.py'
    path = ''  # should be env_root/
    pkg_name = ''  # should be cli namec
    name = '' # author(s) Jim, Bob, Billy
    email = '' # author(s) email same as above
    cmd_line_args = None # setup.py cmd line arguments to run with
    url = False
    lic = False
    short_desc = '' # should be required
    long_desc = False
    pkg_deps = None  # provide as list of strings
    permissions = 0o755


class MainScript(VirtualScript):
    """
    Executable for python package to make CLI accessible
    when package installed
    """
    id = 'main'
    filename = '__main__.py'
    path = '' # should be env_root/bin
    cli_name = '' # is required
    permissions = 0o777
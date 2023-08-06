#!/usr/bin/env python3

import os
import autocleus.cmd as cmd
import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape, StrictUndefined

def find_license(license):
    """
    Return base license class

    Args:
        license(str): name of license file (Apache2, BSD3, MIT)
    """
   
    return cmd.get_module('licenses', modpath='autocleus.library', mod=f'{license}LicenseClass')


def open_source_license(license, env_root, author, email):
    """
    Generates license file at specified path
    
    Args:
        license(object): license object
        env_root(str): virtual environment root directory for project
        author(str): name(s) of project author(s): "Jim Bob, Bob Jim, Kim Tim"
        email(str): email(s) of project authors(s): "jim@bob.com, bob@jim.com,..."
    """

    # Think about rewriting license class to have a write method
    # similar to VirtualScript class.
    # good for now
    lic = find_license(license)
    lic = getattr(lic, f'{license}License')
    
    # renders license from jinja2 template
    rendered_lic = lic.render(name=author, email=email)

    with open(f"{env_root}/LICENSE", "w") as out:
        out.write(rendered_lic)


class classproperty(object):
    '''
    Decorator for class property
    '''
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)
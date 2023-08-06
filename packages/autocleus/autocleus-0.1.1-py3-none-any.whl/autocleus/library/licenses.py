#!/usr/bin/env python3

import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape, StrictUndefined
from autocleus.library import classproperty
from datetime import date

class LicenseClass(type):
    '''
    MetaClass for License classes
    '''

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class License(object):
    """
    Base Virtual License
    """

    __metaclass__ = LicenseClass

    jinja_env = Environment(loader=PackageLoader('autocleus', 'templates'),
                                   autoescape=['.lic'],
                                   undefined=StrictUndefined)

    def __init__(self):
        raise TypeError('License classes are not about to be instantiated')

    @classproperty
    def name(cls):
        name = cls.__doc__
        if not name:
            raise AttributeError('{} has no docstring'.format(cls.__name__))
        return name.strip()

    @classmethod
    def _add_year_to_kwargs(cls, kwargs):
        if 'year' not in kwargs:
            kwargs['year'] = date.today().year
        return kwargs

    @classmethod
    def _check(cls):
        if cls == License:
            raise TypeError('This is a virtual class, do not call it\'s methods')

    @classmethod
    def render(cls, **kwargs):
        """
        Render the LICENSE file
        """
        cls._check()
        kwargs = cls._add_year_to_kwargs(kwargs)
        template = cls.jinja_env.get_template(f"{cls.id}.lic")
        return template.render(**kwargs)

    @classmethod
    def header(cls, **kwargs):
        """
        Render the LICENSE file
        """
        cls._check()
        kwargs = cls._add_year_to_kwargs(kwargs)
        try:
            template = cls.jinja_env.get_template(cls.id + '__header')
            return template.render(**kwargs)
        except jinja2.TemplateNotFound:
            raise AttributeError('{} uses no header'.format(cls.name))


class MITLicense(License):
    """
    The MIT license
    """
    id = 'MIT'
    rpm = 'MIT'
    python = 'License :: OSI Approved :: MIT License'
    url = 'http://opensource.org/licenses/MIT'


class Apache2License(License):
    """
    Apache License Version 2.0
    """
    id = 'Apache-2.0'
    rpm = 'ASL 2.0'
    url = 'https://www.apache.org/licenses/LICENSE-2.0'


class BSD3License(License):
    """
    BSD 3-clause "New" or "Revised" License
    """
    id = 'BSD-3'
    url = 'http://opensource.org/licenses/BSD-3-Clause' 
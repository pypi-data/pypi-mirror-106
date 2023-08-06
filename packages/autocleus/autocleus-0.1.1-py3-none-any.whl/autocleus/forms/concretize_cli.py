#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from PyInquirer import Validator, ValidationError
from setuptools import find_packages
import autocleus.library.styles as styles
from art import *
import os


# interactive form helper functions
def custom_project_directory(answer):
    """Use custom directory for virtual environment root"""
    return not answer['rootdir']


def output_package(answer):
    """Enable prompt for package output path"""
    return ('package and create whl for your CLI' in answer['tasks'] or 
            'output archive of package build (tar)' in answer['tasks'])

def check_for_license(answer):
    """Check if project has a license"""
    return  not answer['check_license']

def add_open_source_license(answer):
    """Enable prompt for OS license type and author(s)"""
    if not answer['check_license']:
        return answer['gen_license']
    else:
        return False

def have_readme(answer):
    """Check if project has a readme"""
    return answer['check_readme']

def projdir_not_cliname(answer):
    return not answer['projname']


def possible_mod_list(env_root, cli_name):
    
    proj_root = f"{env_root}/{cli_name}"
    
    return find_packages(proj_root)

# interactive form validators
class CliNameValidator(Validator):
	
    def validate(self, document):
        try:
            assert str(document.text) == str(document.text).lower()
        except AssertionError:
            raise ValidationError(
                    message="please use lower case for your cli name",
                    cursor_position=len(document.text))

        try:
            assert str(document.text) != 'autocleus'
        except AssertionError:
            raise ValidationError(
                    message="hey now - that's my name!",
                    cursor_position=len(document.text))


class CliDescriptionValidator(Validator):
	
    def validate(self, document):
        try:
            assert len(str(document.text)) <= 80
        except AssertionError:
            raise ValidationError(
                    message="please keep your description to <= 80 chars",
                    cursor_position=len(document.text))



class DirectoryValidator(Validator):

    def validate(self, document):
        try:
            assert os.path.isdir(str(document.text))
        except AssertionError:
            raise ValidationError(
                    message="not a valid directory",
                    cursor_position=len(document.text))

        try:
            assert os.access(str(document.text), os.R_OK)
        except AssertionError:
            raise ValidationError(
                    message="you don't have permission to edit this directory",
                    cursor_position=len(document.text))


class FileValidator(Validator):
    
    def validate(self, document):
        try:
            assert os.path.isfile(str(document.text))
        except AssertionError:
            raise ValidationError(
                    message="not a valid file",
                    cursor_position=len(document.text))

        try:
            assert os.access(str(document.text), os.R_OK)
        except AssertionError:
            raise ValidationError(
                    message="you don't have permission to edit this file",
                    cursor_position=len(document.text))


def process_answers(answers):

    task_map = {'package and create whl for your CLI':'genwhl',
                'generate package spec for your CLI': 'genspec',
                'output archive of package build (tar)': 'gentar'}

    answers['tasks'] = {task_map[task]: task for task in answers['tasks']}

    if 'gen_license' in answers and answers['gen_license']:
        answers['tasks']['oslics'] = 'add open source license'
        answers.pop('check_license')
        answers.pop('gen_license')

    if answers['rootdir']:
        answers['env_root'] = os.getcwd()
        answers.pop('rootdir')

    if answers['check_readme']:
       long_desc = open(answers['long_desc']).read()
       answers['long_desc'] = long_desc

    else:
       answers['long_desc'] = answers['short_desc']
    
    # name project after projdir and cliexe after cli_name
    if answers['projname']:
       answers['projdir'] = answers['cli_name']
       answers.pop('projname')
    
    else:
       answers.pop('projname')

    return answers

def list_modules(list_vals):

    task_list = [Separator("= Python Packages ="), {'name': 'cmd', 'checked': True}]
    list_vals.pop(list_vals.index('cmd'))


    for val in list_vals:
        task_list.append({'name': f"{val}"})

    questions = [
        {
            'type': 'checkbox',
            'name': 'pkgmods',
            'message': 'Which of the following packages should be included with your CLI?',
            'choices': task_list,
        }
    ]

    return prompt(questions, styles=styles.modstyle)

def interactive_form():

    questions = [
        {
            'type': 'checkbox',
            'message': 'Select the work for autocleus to perform:',
            'qmark': 'o',
            'unselected_sign': 'o',
            'name': 'tasks',
            'choices': [
                Separator("= Tasks ="),
                {
		    'name': 'package and create whl for your CLI',
		    'checked': True
                },
                {
                    'name': 'generate package spec for your CLI',
                    'checked': True
                },
		{
		    'name': 'output archive of package build (tar)'
		},
            ],

        },
	{
	    'type': 'confirm',
	    'name': 'rootdir',
	    'message': 'Is the current directory the CLI virtual environment root path?',

	},
	{
	    'type': 'input',
	    'name': 'env_root',
	    'message': "Provide path to CLI virtual environment root:",
	    'when': custom_project_directory,
            'validate': DirectoryValidator
	},
	{
	    'type': 'input',
            'message': 'Provide path to store packaged outputs:',
	    'name': 'output',
	    'when': output_package

	},
	{
	    'type': 'confirm',
	    'message': 'Do you have an open source license for your project?',
	    'name': 'check_license'
	},
	{
	    'type': 'confirm',
	    'message': 'Would you like to generate one?',
	    'name': 'gen_license',
	    'when': check_for_license
	},
	{
            'type': 'list',
            'message': 'Select an open source license to include with your project:',
            'name': 'license',
            'choices': ['Apache-2.0', 'MIT', 'BSD3'],
            'when': add_open_source_license
        },
        {
            'type': 'input',
            'message': 'Provide the authour(s) for the licese (e.g. Bob, Bill, Jim):',
            'name': 'author',
            'when': add_open_source_license
        },
	{
	    'type': 'input',
	    'message': 'Provide email(s) to include in license file (e.g. bob@email.com, bill@email.com, jim@email.com)',
	    'name': 'email',
	    'when': add_open_source_license
        },
	{
	    'type': 'confirm',
	    'message': 'Do you have a README file for your CLI?',
	    'name': 'check_readme'
	},
	{
	    'type': 'input',
	    'message': 'Provide the path to your README file:',
	    'name': 'long_desc',
	    'when': have_readme,
            'validate': FileValidator
	},
        {
	    'type': 'input',
	    'message': 'Provide a short description of your CLI:',
	    'name': 'short_desc',
	    'validate': CliDescriptionValidator
	},
	{
	    'type': 'input',
	    'message': 'What would you like to call your CLI?',
	    'name': 'cli_name',
	    'validate': CliNameValidator
        },
        {
            'type': 'confirm',
            'message': 'Is your CLI project root directory named the same as your CLI?',
            'name': 'projname'
        },
        {
            'type': 'input',
            'message': 'What is the name of your CLI project root directory?',
            'name': 'projdir',
            'when': projdir_not_cliname
        },
	{
	    'type': 'input',
	    'message': 'Provide a version number for your CLI:',
	    'name': 'version'
        }
    ]
    answers = prompt(questions, style=styles.formstyle())
    # should move these out of this function and into command (to get Cancelled by User warning).
    if projdir_not_cliname(answers):
        mods = possible_mod_list(answers['env_root'], answers['projdir'])
    else:
        mods = possible_mod_list(answers['env_root'], answers['cli_name'])
    modules = list_modules(mods)
    answers['pkgmods'] = modules['pkgmods']


    return process_answers(answers)

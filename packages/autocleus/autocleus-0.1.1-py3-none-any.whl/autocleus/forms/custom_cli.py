#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from PyInquirer import Validator, ValidationError
import autocleus.library.styles as styles
from art import *
import os


# interactive form helper functions
def custom_project_directory(answer):
	"""Setup custom project directory - enables prompt for path definition"""
	return not answer['rootdir']


def preinstall_packages(answer):
    """Enable prompt for list of packages or path to requirments.txt"""
    return "preinstall python packages" in answer['tasks']


def add_open_source_license(answer):
    """Enable prompt for OS license type and author(s)"""
    return "add open source license" in answer['tasks']


def cookiecutter_project(answer):
	"""
	Enable prompt to deploy cookiecutter template
	"""
	return "cookiecutter" in answer['tasks']


# interactive form validators
class CLINameValidator(Validator):
    """
    Validate CLI name, must be lower case and must not be 
    autocleus :)
    """	
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


class CLIDescriptionValidator(Validator):
    """
    Validate CLI description, limited to 80 charcters or less
    """
    def validate(self, document):
        try:
            assert len(document.text) <= 80
        except AssertionError:
            raise ValidationError(
                    message="short description must be <= 80 charcters",
                    cursor_position=len(document.text))

def interactive_form():

    # before printing form print out header "Autocleus - Here to serve not to be served"
    
    #tprint('Autocleus', font='bulbhead')
    #print('Here to serve not to be served')
    #styles.autocleus_banner()

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
		    'name':'generate command template',
		    'checked': True,
                },
		{
		    'name': 'generate cli executable',
		    'checked': True
	        },
		{
		    'name': 'preinstall python packages'
		},
		{	
				    'name': 'add open source license'
		},
            ],

        },
        {
                'type': 'confirm',
                'name': 'rootdir',
                'message': 'Is the current directory the intended project root directory?'

        },
        {
                'type': 'input',
                'name': 'projdir',
                'message': "Provide path to project directory (it doesn't need to exist):",
                'when': custom_project_directory
        },
        {
                'type': 'input',
                'message': 'Please provide a space separated list of python package names to install or absolute path to requirements.txt:',
                'name': 'pkgs',
                'when': preinstall_packages

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
                'type': 'input',
                'message': 'What would you like to call your CLI?',
                'name': 'cli_name',
                'validate': CLINameValidator
        },
        {
                'type': 'input',
                'message': 'Please provide a short description of your CLI',
                'name': 'cli_desc',
                'validate': CLIDescriptionValidator
        }
    ]
    answers = prompt(questions, style=styles.formstyle())
    return process_answers(answers)

def process_answers(answers):
    # add abbreviated keys for tasks
    
    lic_map = {'Apache-2.0': 'Apache2', 'MIT': 'MIT', 'BSD3': 'BSD3'}

    task_map = {'generate command template':'cmd_template', 
                'generate cli executable': 'cliexe', 
                'preinstall python packages': 'pkgs', 
                'add open source license': 'oslics'}
    answers['tasks'] = {task_map[task]: task for task in answers['tasks']}
    
    # add current directory as env_root path to answers dictionary
    if 'rootdir' in answers:
        cwd = os.getcwd()
        answers['env_root'] = cwd

    # if current directory isn't project directory set env_root to user defined path
    if 'projdir' in answers:
        answers['env_root'] = answers.pop('projdir')

    if 'license' in answers:
        answers['license'] = lic_map[answers['license']]

    return answers

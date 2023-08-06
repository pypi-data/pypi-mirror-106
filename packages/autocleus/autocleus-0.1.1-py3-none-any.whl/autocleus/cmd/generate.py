#!/usr/bin/env python3

from autocleus.forms import custom_cli as iform 
from autocleus.forms import concretize_cli as cform
from autocleus.library import styles
from autocleus.hooks.custom_cli import customCLI
#from autocleus.hooks.concretize import concretizeCLI


description = "Create CLI virtual environment for dev and/or concretize your CLI"
section = "build"
level = "short"


def setup_parser(subparser):
    """"Setup command subparser"""
    
    # add arguments for data command
    subparser.add_argument('--custom_cli', action='store_true',
            help="create dev environment for custom cli as virtualenv")

    subparser.add_argument('--concretized_cli', action='store_true',
            help="concretize custom cli virtualenv into cli installer")


def generate(parser, args):
    """Monitor transfer"""
    actions = parser.parse_args()

    if vars(actions)['custom_cli']:
        # create virtual env for developing cli
        styles.autocleus_banner()
        opts = iform.interactive_form()
        customCLI(chdir=opts['env_root'], **opts).call()

    elif vars(actions)['concretized_cli']:
        # concretize and generate whl for cli from venv
        styles.autocleus_banner()
        opts = cform.interactive_form()
        print(opts)

    else:
        # nothing to do here
        exit("must specify action")

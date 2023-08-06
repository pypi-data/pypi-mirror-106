#!/usr/bin/env python3

import re
import sys
import argparse
import autocleus.cmd as cmd
from autocleus.library.parsers import BaseArgumentParser, FancyHelpFormatter

levels = ['short', 'long']


def initiate_argument_parser(**kwargs):
    """Create a basic argument parser with no subcommands added"""
    parser = BaseArgumentParser(
            formatter_class=FancyHelpFormatter, add_help=False,
            description=(
            "A CLI for creating CLIs in Python, easily."))

    parser.add_argument('-h', '--help', dest='help', action='store_const',
            const='short', default=None, help="Show this help message")

    parser.add_argument('-H', '--all-help', dest='help', action='store_const',
            const='long', default=None, help="Show help for all commands")
    
    return parser



def main(argv=None):
    """Entry point for all commands"""

    parser = initiate_argument_parser()
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args, unknown = parser.parse_known_args(sys.argv)

    #if 'help' in list(vars(args).keys()):
    #    sys.stdout.write(parser.format_help(level=args.help))
    #    return 0
    #elif not args.command:
    #    parser.print_help()
    #    return 1
    
    cmd_name = args.command[1]#.translate({ord(i): None for i in './'})
    
    command = parser.add_command(cmd_name)

    # Re-parse with the proper sub-parser added.
    args, unknown = parser.parse_known_args()
    
    command(parser, args)
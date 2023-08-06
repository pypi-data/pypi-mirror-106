#!/usr/bin/env python3

import sys
import argparse
import autocleus.cmd as cmd
from autocleus.library.parsers import BaseArgumentParser, FancyHelpFormatter


class CLImaker():

    def __init__(self, cmdpath, cli_description):
        self.modpath = cmdpath
        self.cli_description = cli_description

    def entrypoint(self):
        """Entry point for all commands"""

        parser = self.initiate_argument_parser()
        parser.add_argument('command', nargs=argparse.REMAINDER)
        args, unknown = parser.parse_known_args(sys.argv)

        #if 'help' in list(vars(args).keys()):
        #    sys.stdout.write(parser.format_help(level=args.help))
        #    return 0
        #elif not args.command:
        #    parser.print_help()
        #    return 1
    
        cmd_name = args.command[1]#.translate({ord(i): None for i in './'})
    
        command = parser.add_command(cmd_name, modpath=self.modpath)

        # Re-parse with the proper sub-parser added.
        args, unknown = parser.parse_known_args()
    
        command(parser, args)

    def initiate_argument_parser(self, **kwargs):
        """Create a basic argument parser with no subcommands added"""
        parser = BaseArgumentParser(
            formatter_class=FancyHelpFormatter, add_help=False,
            description=(f"{self.cli_description}"))

        parser.add_argument('-h', '--help', dest='help', action='store_const',
                const='short', default=None, help="Show this help message")

        parser.add_argument('-H', '--all-help', dest='help', action='store_const',
                const='long', default=None, help="Show help for all commands")
    
        return parser
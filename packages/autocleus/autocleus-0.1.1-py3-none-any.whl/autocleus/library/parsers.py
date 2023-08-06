import re
import sys
import argparse
import autocleus.cmd as cmd

levels = ['short', 'long']

def index_commands():
    """create an index of commands by section for this help level"""
    index = {}
    for command in spack.cmd.all_commands():
        cmd_module = spack.cmd.get_module(command)

        # make sure command modules have required properties
        for p in required_command_properties:
            prop = getattr(cmd_module, p, None)
            if not prop:
                tty.die("Command doesn't define a property '%s': %s"
                        % (p, command))

        # add commands to lists for their level and higher levels
        for level in reversed(levels):
            level_sections = index.setdefault(level, {})
            commands = level_sections.setdefault(cmd_module.section, [])
            commands.append(command)
            if level == cmd_module.level:
                break

    return index

class FancyHelpFormatter(argparse.RawTextHelpFormatter):
    def _format_actions_usage(self, actions, groups):
        """
        Formatter with more concise usage of strings
        """

        usage = super(
                FancyHelpFormatter, self)._format_actions_usage(actions, groups)

        # compress single-character flags that are not mutulally exclusive
        # at the beggining of the usage string

        chars = ''.join(re.findall(r'\[-(.)\]', usage))
        usage = re.sub(r'\[-.\] ?', '', usage)
        if chars:
            return '[-%s] %s' % (chars, usage)
        else:
            return usage


class BaseArgumentParser(argparse.ArgumentParser):

    def format_help_sections(self, level):
        """
        Format help on sections for a particular verbosity level.
        Args:
        level (str): 'short' or 'long' (more commands shown for long)
        """
        if level not in levels:
            raise ValueError("level must be one of: %s" % levels)

        # lazily add all commands to the parser when needed.
        add_all_commands(self)

        """Print help on subcommands in neatly formatted sections."""
        formatter = self._get_formatter()

        # Create a list of subcommand actions. Argparse internals are nasty!
        # Note: you can only call _get_subactions() once.  Even nastier!
        if not hasattr(self, 'actions'):
            self.actions = self._subparsers._actions[-1]._get_subactions()

        # make a set of commands not yet added.
        remaining = set(monTransfer.cmd.all_commands())

        def add_group(group):
            formatter.start_section(group.title)
            formatter.add_text(group.description)
            formatter.add_arguments(group._group_actions)
            formatter.end_section()

        def add_subcommand_group(title, commands):
            """Add informational help group for a specific subcommand set."""
            cmd_set = set(c for c in commands)

            # make a dict of commands of interest
            cmds = dict((a.dest, a) for a in self.actions
                        if a.dest in cmd_set)

            # add commands to a group in order, and add the group
            group = argparse._ArgumentGroup(self, title=title)
            for name in commands:
                group._add_action(cmds[name])
                if name in remaining:
                    remaining.remove(name)
            add_group(group)

        # select only the options for the particular level we're showing.
        show_options = options_by_level[level]
        if show_options != 'all':
            opts = dict((opt.option_strings[0].strip('-'), opt)
                        for opt in self._optionals._group_actions)

            new_actions = [opts[letter] for letter in show_options]
            self._optionals._group_actions = new_actions

        # custom, more concise usage for top level
        help_options = self._optionals._group_actions
        help_options = help_options + [self._positionals._group_actions[-1]]
        formatter.add_usage(
            self.usage, help_options, self._mutually_exclusive_groups)

        # description
        formatter.add_text(self.description)

        # start subcommands
        formatter.add_text(intro_by_level[level])

        # add argument groups based on metadata in commands
        index = index_commands()
        sections = index[level]

        for section in sorted(sections):
            if section == 'help':
                continue   # Cover help in the epilog.

            group_description = section_descriptions.get(section, section)

            to_display = sections[section]
            commands = []

            # add commands whose order we care about first.
            if section in section_order:
                commands.extend(cmd for cmd in section_order[section]
                                if cmd in to_display)

            # add rest in alphabetical order.
            commands.extend(cmd for cmd in sorted(sections[section])
                            if cmd not in commands)

            # add the group to the parser
            add_subcommand_group(group_description, commands)

        # optionals
        add_group(self._optionals)

        # epilog
        formatter.add_text("""\
{help}:
autocleus help --all       list all commands and options
autocleus help <command>   help on a specific command
""".format(help=section_descriptions['help']))

        # determine help from format above
        return formatter.format_help()


    def add_subparsers(self, **kwargs):
        """Ensure that sensible defaults are propagated to subparsers"""
        kwargs.setdefault('metavar', 'SUBCOMMAND')
        sp = super(BaseArgumentParser, self).add_subparsers(**kwargs)
        old_add_parser = sp.add_parser

        def add_parser(name, **kwargs):
            kwargs.setdefault('formatter_class', FancyHelpFormatter)
            return old_add_parser(name, **kwargs)
        
        sp.add_parser = add_parser
        return sp

    def add_command(self, cmd_name, **kwargs):
        """Add one subcommand to this parser."""
        # lazily initialize any subparsers
        if not hasattr(self, 'subparsers'):
            # remove the dummy "command" argument.
            if self._actions[-1].dest == 'command':
                self._remove_action(self._actions[-1])
            self.subparsers = self.add_subparsers(metavar='COMMAND',
                                                  dest="command")

        # each command module implements a parser() function, to which we
        # pass its subparser for setup.
        module = None
        if 'modpath' in kwargs:
            module = cmd.get_module(cmd_name, modpath=kwargs['modpath'])
        else:
            module = cmd.get_module(cmd_name)
        subparser = self.subparsers.add_parser(cmd_name,
            help=module.description, description=module.description)
        
        module.setup_parser(subparser)
        
        # return the callable function for the command
        if 'modpath' in kwargs:
            return cmd.get_command(cmd_name, modpath=kwargs['modpath'])
        else:
            return cmd.get_command(cmd_name)


    def format_help(self, level='short'):
        print(self.prog)
        if self.prog == 'monty':
            # use format_help_sections for the main spack parser, but not
            # for subparsers
            return self.format_help_sections(level)
        else:
            # in subparsers, self.prog is, e.g., 'spack install'
            return super(BaseArgumentParser, self).format_help()


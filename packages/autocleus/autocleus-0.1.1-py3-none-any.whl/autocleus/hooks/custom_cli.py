#!/usr/bin/env python3

import autocleus
import autocleus.hooks as hooks
from autocleus.hooks import BaseHook
import autocleus.library.venv_utils as virtenv
from pydantic import BaseModel, SecretStr, BaseSettings, Extra, ValidationError, validator
from typing import Dict, Any, Union, Type, List, Optional
import os
import time
from yaspin import yaspin

# Probably want to separate hooks as this file could become overloaded in future
class customCLITaskList(BaseModel):
    cmd_template: Optional[str] = ''
    cliexe: Optional[str] = ''
    pkgs: Optional[str] = ''
    oslics: Optional[str] = ''

class customCLI(BaseHook):
    
    tasks: customCLITaskList
    env_root: str
    cli_name: str
    cli_desc: str
    rootdir: str
    pkgs: Optional[str] = ''
    license: Optional[str] = ''
    author: Optional[str] = ''
    email: Optional[str] = ''
    
    def execute(self):
        """Carry out user specified tasks"""

        # create virtual environment in env_root
        with yaspin(text='Creating virtual environment for your CLI', color='cyan') as sp:
            virtenv.create_virtualenv(self.env_root)
            autocleus.default_project_directory(self.env_root, self.cli_name)
            sp.ok("[OK] ")
        
        if self.tasks.cmd_template:
            # create comSand template in cmd directory of project
            with yaspin(text="Generating command template", color='cyan') as sp:
                autocleus.command_template(self.env_root, self.cli_name)
                time.sleep(1)
                sp.ok("[OK] ")
                
        if self.tasks.cliexe:
            # create cli executable in virtual environment
            with yaspin(text="Generating CLI executable", color='cyan') as sp:
                autocleus.dev_cliexe(self.env_root, self.cli_name, self.cli_desc)
                time.sleep(1)
                sp.ok("[OK] ")
                            
        if self.tasks.pkgs:
            # install packages into virtual environmen
            # they can provide a string pkg1, pkg2, etc.. or a path to a requirements.text 
            # note: autocleus and all of it's dependencies will need to be installed at minimum
            # perhaps move the with statement to before each for loop and show "Installing <package name> ..."
            with yaspin(text="Installing Python packages into virtual environment", color='cyan') as sp:
                
                if os.path.isfile(self.pkgs):
                    # install packages from requirements.txt
                    with open(self.pkgs) as reqs:
                        pkgs_list = reqs.readlines()
                        pkg_list = [i.strip() for i in pkg_list]    
            
                    virtenv.install_packages_to_venv(self.env_root, pkg_list)

                # add Exception for if both of these fail: something to allow 
                # re-entering packages
                else:
                    # install packages from string listed on command line
                    virtenv.install_packages_to_venv(self.env_root, self.pkgs.split())

                sp.ok("[OK] ")

        if self.tasks.oslics:
            # generate LICENSE file in root directory
            with yaspin(text=f'Generating {self.license} license for project', color='cyan') as sp:
                autocleus.library.open_source_license(self.license, self.env_root, 
                                                            self.author, self.email)
                time.sleep(1.0)
                sp.ok("[OK] ")

        with yaspin(text='Installing autocleus to the virtual environment', color='cyan') as sp:
            virtenv.install_packages_to_venv(self.env_root, ['autocleus'])
            sp.ok("[OK] ")
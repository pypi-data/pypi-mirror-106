class InstallCLI(Command):
    # Experimental class to install __main__.py from python code object by adding this to 
    # setup.py cmd_classes : check setuptools.command.build_py
    #https://stackoverflow.com/questions/677577/distutils-how-to-pass-a-user-defined-parameter-to-setup-py
    # https://jichu4n.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy/
    # The idea behind this is so that the __main__.py that becomes the executable for the cli is
    # installed to a specific location that is on users path - ::: currently thinking of using
    # sys.path.
    description = "Install CLI executable and adds to PATH"
    user_options = [
        ('cliname=', 'c', 'Specify CLI name'),
        ('script-dir=', 's', 'install scripts to DIR'),
        ('script-content=', 'e', 'Specify content of CLI entrypoint script')
    ]

    """
    This ultimately becomes another command line option when running setup.py:

    setuptools.setup(
    cmdclass={
        'install_cli': InstallCLI,
    },
    # Usual setup() args.
    # ...
    )

    The above added to the setup.py you can then run: python3 setup.py install_cli --script-dir=/path/to/dir

    You would pass this to sys.argv[:] = ['setup.py'] + user_optios before using _execfile like
    in run method in class below.
    """
    
    def initialize_options(self):
        self.cliname = None
        self.script_dir = None
        self.script_content = None
        

  def finalize_options(self):
    """Post-process options."""
    assert self.cliname not None and self.entryscript not None, (
    f'Both cliname ({self.cliname}) and entrypscript ({self.entryscript})must be defined')


    def run(self):
        # These needs to take a python code object and convert it 
        # setup.py will include this method
        # it will install the clie executable from a rendered template
        # rendered to string.
        from setuptools.command.easy_install import chmod, current_umask


    def write_script(self, mode="t", *ignored):
        """Write an executable file to the scripts directory"""
        from setuptools.command.easy_install import chmod, current_umask

        log.info(f"Installing {self.cliname} script to {self.script_dir}")
        
        # target should be added to ch
        target = os.path.join(self.script_dir, cliname)
        

        # need to review this
        mask = current_umask():
        ensure_directory(target)
            f = open(target, "w" + mode)
            f.write(contents)
            f.close()
            chmod(target, 0o777 - mask)
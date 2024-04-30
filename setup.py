import os
from pkg_resources import parse_requirements
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils import log

install_reqs = parse_requirements('requirements.txt')

class OverrideInstall(install):
    """
    Set mode of scripts to "runnable"
    """

    def run(self):
        mode = 0o700
        install.run(self)
        for filepath in self.get_outputs():
            if self.install_scripts in filepath:
                log.info("Overriding setuptools mode of scripts ...")
                log.info("Changing permissions of %s to %s" %
                         (filepath, oct(mode)))
                os.chmod(filepath, mode)

setup(
    name='cyb_600_lab3_client',
    version='1.0.0',
    author_email='kourkouk@canisius.edu',
    author='Riley Kourkounis',
    packages=find_packages(
        where='src',
    ),
    test_suite="tests",
    package_dir={"": "src"},
    license='Apache License Version 2.0',
    cmdclass={'install': OverrideInstall}
)

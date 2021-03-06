"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="report",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Click','pandas'],
    entry_points={
        'console_scripts' : 
        ['report = src.main:start']
    },

)
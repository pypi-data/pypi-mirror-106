import setuptools
from setuptools import version, find_packages
from pathlib import Path
# it has a function called setup
# it has some important keywords arg
# firstone is name remember to make a unique name
# next one is version set it to 1.0
# we need a long_description
# also we need to tell python about the packagse that sre going to be distributed
# also we need to exclude data and test subfolders
setuptools.setup(
    name="majedutdPDF",
    version=1.1,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=("test", "data"))
)

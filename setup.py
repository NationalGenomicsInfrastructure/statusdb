from setuptools import setup, find_packages

try:
    with open("requirements.txt", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
    install_requires = []

setup(name = "statusdb",
    version = "1.0.0",
    author = "Science for Life Laboratory",
    author_email = "genomics_support@scilifelab.se",
    description = ("Module for connecting to statusdb and retrieve "
                   "required information from available module within "),
    install_requires = install_requires,
    packages = find_packages()
    )

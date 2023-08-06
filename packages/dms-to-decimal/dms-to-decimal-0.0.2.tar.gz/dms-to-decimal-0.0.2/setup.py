from os import path
from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'dms to decimal'
directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
        name="dms-to-decimal", 
        version=VERSION,
        author="Reagan Scofield",
        author_email="scofieldreagan@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords= [
            "python",
            "pip",
            "DMS",
            "decimal",
            "degree",
            "minute",
            "second"
        ],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
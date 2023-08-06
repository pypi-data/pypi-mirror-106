from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'dms to decimal'
LONG_DESCRIPTION = 'A Python library for converting degrees, minutes, and seconds to decimal'

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
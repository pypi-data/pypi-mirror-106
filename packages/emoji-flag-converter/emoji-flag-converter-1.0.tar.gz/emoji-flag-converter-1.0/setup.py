from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'Emoji Flag Converter'
LONG_DESCRIPTION = 'Converts a country code/name into a flag emoji'

setup(
       # the name must match the folder name 'verysimplemodule'
        name="emoji-flag-converter",
        version="1.0",
        author="Steven Yu",
        author_email="stevenyuser@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],

        keywords=['python', 'emoji flag'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)

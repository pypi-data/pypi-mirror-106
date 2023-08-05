import setuptools
from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A basic hello package'
LONG_DESCRIPTION = 'A basic hello package'


# Setting up
setuptools.setup(
    name="bosons",
    version=VERSION,
    author="Glauco",
    author_email="<glauco.endrigo@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ]
)

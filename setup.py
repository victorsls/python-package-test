import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A test Python package'
LONG_DESCRIPTION = 'A test Python package, to validate the creation of a new package.'

setup(
    name="python-package-test",
    version=VERSION,
    author="Victor Rafael",
    author_email="<victorsls@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[""],
    keywords=['python'],
    classifiers=[]
)

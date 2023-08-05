from setuptools import setup, find_packages
import codecs
import os
import pathlib

here = os.path.abspath(os.path.dirname(__file__))
HERE = pathlib.Path(__file__).parent

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Extract lines external file'
LONG_DESCRIPTION = 'Extract lines external file'
README = (HERE / "README.md").read_text()
# Setting up
setup(
    name="abqos",
    version=VERSION,
    author="Abraham Pérez",
    author_email="abraham1798@gmail.com",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pynput'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

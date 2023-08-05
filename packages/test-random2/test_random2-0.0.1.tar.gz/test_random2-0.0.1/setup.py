from setuptools import setup, find_packages
import pkg_resources
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'little module that helps to create tables for a specified schema with random content'
LONG_DESCRIPTION = 'little module that helps to create tables for a specified schema with random content'

# Setting up
setup(
    name="test_random2",
    version=VERSION,
    author="detective (Maxim Perl)",
    author_email="<Maxim.Perl@detective.solutions>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['data/*.csv']},
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'pandas', 'numpy', 'tables', 'data', 'data science'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
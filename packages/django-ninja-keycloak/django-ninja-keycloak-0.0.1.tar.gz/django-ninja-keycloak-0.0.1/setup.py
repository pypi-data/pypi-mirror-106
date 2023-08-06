from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Django Ninja package to integrate keycloak authentication'
LONG_DESCRIPTION = 'A package that allows to build keycloak based authentication.'

# Setting up
setup(
    name="django-ninja-keycloak",
    version=VERSION,
    author="kgaulin (Kevin Gaulin)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python-keycloak', 'django-ninja'],
    keywords=['python', 'django-ninja', 'keycloak'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
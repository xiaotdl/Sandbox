Ref:
http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

# The Hitchhiker’s Guide to Packaging

## Quick Start

1. Lay out your project

TowelStuff/
    LICENSE.txt
    README.txt
    setup.py
    towelstuff/
        __init__.py


2. Describe your project
The setup.py file is at the heart of a Python project.
It describes all of the metadata about your project.
Only three required fields: name, version, and packages.

setup.py
"""
from distutils.core import setup

setup(
    name='TowelStuff',
    version='0.1dev',
    packages=['towelstuff',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
"""


3. Create your first release

$ python setup.py sdist

==> dist/TowelStuff-0.1.tar.gz

TowelStuff$ cat MANIFEST
# file GENERATED by distutils, do NOT edit
README.txt
setup.py
towelstuff/__init__.py


4. Register your package with the Python Package Index (PyPI)
The distribution file generated by running sdist can be published anywhere.
There is a central index of all publically available Python projects maintained on the python.org web site named the The Python Package Index (PyPI).
This is where you will want to release your distribution if you intend to make your project public.

You will first have to visit that site, where you can register for an account.

Project’s are published on PyPI in the format of:
http://pypi.python.org/pypi/<projectname>

Your project will have to choose a name which is not already taken on PyPI. You can then claim your new project’s name by registering the package by running the command:

$ python setup.py register


5. Upload your release, then grab your towel and save the Universe!

$ python setup.py sdist bdist_wininst upload

At this point you should announce your package to the community!

Finally, in your setup.py you can make plans for your next release, by changing the version field to indicate which version you want to work towards next (e.g. 0.2dev).


## Introduction to Packaging

This document describes the current state of packaging in Python using Distribution Utilities (“Distutils”) and its extensions from the end-user’s point-of-view, describing how to extend the capabilities of a standard Python installation by building packages and installing third-party packages, modules and extensions.

Python has a packaging system that allows people to distribute their programs and libraries in a standard format that makes it easy to install and use them. In addition to distributing a package, Python also provides a central service for contributing packages. This service is known as The Python Package Index (PyPI). Information about The Python Package Index (PyPI) will be provided throughout this documentation. This allows a developer to distribute a package to the greater community with little effort.


### The Packaging Ecosystem

#### A Package
A package is simply a directory with an __init__.py file inside it. For example:
"""
$ mkdir mypackage
$ cd mypackage
$ touch __init__.py
$ echo "# A Package" > __init__.py
$ cd ..
"""

"""
$ ls
mypackage
$ python
>>> import mypackage
>>> mypackage.__file__
'mypackage/__init__.py'
"""

#### Discovering a Python Package
"""
>>> import sys
>>> import pprint
>>> pprint.pprint(sys.path)
['',
 '/usr/lib/python2.7',
 '/usr/lib/python2.7/plat-x86_64-linux-gnu',
 '/usr/lib/python2.7/lib-tk',
 '/usr/lib/python2.7/lib-old',
 '/usr/lib/python2.7/lib-dynload',
 '/home/xili/.local/lib/python2.7/site-packages',
 '/usr/local/lib/python2.7/dist-packages',
 '/usr/lib/python2.7/dist-packages']
>>> import mypackage
>>> mypackage.__file__
'mypackage/__init__.py'
"""

The first value, the null or empty string, in sys.path is the current working directory, which is what allows the packages in the current working directory to be found.

#### Explicitly Including a Package Location
The convention way of manually installing packages is to put them in the .../site-packages/ directory.

In order to import them, this directory must be added to sys.path. There are several different ways to add the directory.

1) through .pth config file
The most convenient way is to add a path configuration file to a directory that’s already in Python’s path, which could be the .../site-packages/ directory. Path configuration files have an extension of .pth, and each line must contain a single path that will be appended to sys.path. (Because the new paths are appended to sys.path, modules in the added directories will not override standard modules. This means you can’t use this mechanism for installing fixed versions of standard modules.)

Paths can be absolute or relative, in which case they’re relative to the directory containing the .pth file. See the documentation of the site module for more information.

2) through PYTHONHOME env var
In addition there are two environment variables that can modify sys.path.
PYTHONHOME sets an alternate value for the prefix of the Python installation. For example, if PYTHONHOME is set to /www/python/lib/python2.6/, the search path will be set to ['', '/www/python/lib/python2.6/', ...].

The PYTHONPATH variable can be set to a list of paths that will be added to the beginning of sys.path. For example, if PYTHONPATH is set to /www/python:/opt/py, the search path will begin with ['', '/www/python', '/opt/py', ...].

3) thourgh modify sys.path
Finally, sys.path is just a regular Python list, so any Python application can modify it by adding or removing entries.

== zc.buildout ==
The zc.buildout package modifies the sys.path in order to include all packages relative to a buildout. The zc.buildout package is often used to build large projects that have external build requirements.


#### Python file layout
A Python installation has a site-packages directory inside the module directory. This directory is where user installed packages are dropped. A .pth file in this directory is maintained which contains paths to the directories where the extra packages are installed.


#### Benefits of packaging
While it’s possible to unpack tarballs and manually put them into your Python installation directories (see Explicitly Including a Package Location), using a package management system gives you some significant benefits.
Here are some of the obvious ones:
- Dependency management
- Accounting
- Uninstall
- Search


#### Current State of Packaging

Future os Packaging
In short...
setup.py gone!
distutils gone!
distribute gone!
pip and virtualenv here to stay!
eggs ... gone!


































































































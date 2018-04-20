Ref:
https://packaging.python.org/

# Python Packaging User Guide

== Get started ==
Essential tools and concepts for working with the Python packaging ecosystem are covered in our Tutorials section:
- to learn how to install packages, see the **tutorial on installing packages**.
- to learn how to manage dependencies in a version controlled project, see the **tutorial on managing application dependencies**.
- to learn how to package and distribute your projects, see the tutorial on **packaging and distributing**


## Tutorials

### Installing Packages

> Ensure pip, setuptools, and wheel are up to date
"""
python -m pip install --upgrade pip setuptools wheel
"""


> Optionally, create a virtual environment
"""
python3 -m venv tutorial_env
source tutorial_env/bin/activate
"""


> Use pip for Installing
"""
To install the latest version of “SomeProject”:
pip install 'SomeProject'

To install a specific version:
pip install 'SomeProject==1.4'

To install greater than or equal to one version and less than another:
pip install 'SomeProject>=1,<2'

To install a version that’s “compatible” with a certain version: [4]
pip install 'SomeProject~=1.4.2'
"""


> Requirements files
Install a list of requirements specified in a Requirements File.
"""
pip install -r requirements.txt
"""


> Source Distributions vs Wheels
pip can install from either Source Distributions (sdist) or Wheels, but if both are present on PyPI, pip will prefer a compatible wheel.

Wheels are a pre-built distribution format that provides faster installation compared to Source Distributions (sdist), especially when a project contains compiled extensions.

If pip does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.


> Installing from VCS
Install a project from VCS in “editable” mode. For a full breakdown of the syntax, see pip’s section on VCS Support.
"""
pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
pip install -e hg+https://hg.repo/some_pkg#egg=SomeProject                # from mercurial
pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomeProject  # from a branch
"""
Ref: https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support


> Installing from other Indexes
"""
pip install --index-url http://my.package.repo/simple/ SomeProject
"""


> Installing from a local src tree
"""
pip install <path>
"""


### Managing Application Dependencies

intro to pipenv...


### Packaging and distributing projects

#### Configuring your project

== Initial files ==

*setup.py*
The most important file is setup.py which exists at the root of your project directory. For an example, see the setup.py in the PyPA sample project.
- It’s the file where various aspects of your project are configured. The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined. The most relevant arguments are explained in the section below.

- It’s the command line interface for running various commands that relate to packaging tasks.

*setup.cfg*
setup.cfg is an ini file that contains option defaults for setup.py commands.

*README.rst / README.md*

*MANIFEST.in*
A MANIFEST.in is needed when you need to package additional files that are not automatically included in a source distribution.

*LICENSE.txt*
Every package should include a license file detailing the terms of distribution. In many jurisdictions, packages without an explicit license can not be legally used or distributed by anyone other than the copyright holder. If you’re unsure which license to choose, you can use resources such as GitHub’s Choose a License or consult a lawyer.

*<your package>*
Although it’s not required, the most common practice is to include your Python modules and packages under a single top-level package that has the same name as your project, or something very close.

*setup() args*
name='projectname',

version='1.2.0',
e.g.
1.2.0.dev1  # Development release
1.2.0a1     # Alpha Release
1.2.0b1     # Beta Release
1.2.0rc1    # Release Candidate
1.2.0       # Final Release
1.2.0.post1 # Post Release
15.10       # Date based release
23          # Serial release

description='A sample Python project',
long_description=long_description,
long_description_content_type='text/x-rst',

url='https://github.com/pypa/sampleproject',
Give a homepage URL for your project.

author='The Python Packaging Authority',
author_email='pypa-dev@googlegroups.com',
Provide details about the author.

license='MIT',

classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
],


keywords
keywords='sample setuptools development',

project_urls
project_urls={
    'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
    'Funding': 'https://donate.pypi.org',
    'Say Thanks!': 'http://saythanks.io/to/example',
    'Source': 'https://github.com/pypa/sampleproject/',
    'Tracker': 'https://github.com/pypa/sampleproject/issues',
},

packages
packages=find_packages(exclude=['contrib', 'docs', 'tests\*']),
It is required to list the packages to be included in your project. Although they can be listed manually, setuptools.find_packages finds them automatically. Use the exclude keyword argument to omit packages that are not intended to be released and installed.

install_requires
install_requires=['peppercorn'],
“install_requires” should be used to specify what dependencies a project minimally needs to run. When the project is installed by pip, this is the specification that is used to install its dependencies.

python_requires
If your project only runs on certain Python versions, setting the python_requires argument to the appropriate PEP 440 version specifier string will prevent pip from installing the project on other Python versions. For example, if your package is for Python 3+ only, write:

"""
python_requires='>=3',
python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.\*, <4',
"""

package_data
package_data={
    'sample': ['package_data.dat'],
},
Often, additional files need to be installed into a package. These files are often data that’s closely related to the package’s implementation, or text files containing documentation that might be of interest to programmers using the package. These files are called “package data”.

data_files
data_files=[('my_data', ['data/data_file'])],
Although configuring package_data is sufficient for most needs, in some cases you may need to place data files outside of your packages. The data_files directive allows you to do that.

py_modules
py_modules=["six"],
It is required to list the names of single file modules that are to be included in your project.

#### Working in “development mode”
Assuming you’re in the root of your project directory, then run:

pip install -e .
Although somewhat cryptic, -e is short for --editable


 For example, supposing your project requires “foo” and “bar”, but you want “bar” installed from VCS in editable mode, then you could construct a requirements file like so:
-e .
-e git+https://somerepo/bar.git#egg=bar


#### Packaging your project

== Source distributions ==
python setup.py sdist


== Wheels ==
You should also create a wheel for your project. A wheel is a built package that can be installed without needing to go through the “build” process. Installing wheels is substantially faster for the end user than installing from a source distribution.

If your project is pure Python (i.e. contains no compiled extensions) and natively supports both Python 2 and 3, then you’ll be creating what’s called a *Universal Wheel* (see section below).

If your project is pure Python but does not natively support both Python 2 and 3, then you’ll be creating a “Pure Python Wheel” (see section below).

If your project contains compiled extensions, then you’ll be creating what’s called a *Platform Wheel* (see section below).

Before you can build wheels for your project, you’ll need to install the wheel package:
pip install wheel

== Universal Wheels ==
To build the wheel:
"""
python setup.py bdist_wheel --universal
"""

You can also permanently set the --universal flag in setup.cfg (e.g., see sampleproject/setup.cfg):
[bdist_wheel]
universal=1

Only use the --universal setting, if:
1. Your project runs on Python 2 and 3 with no changes (i.e. it does not require 2to3).
2. Your project does not have any C extensions.

== Pure Python Wheels ==
Pure Python Wheels that are not “universal” are wheels that are pure Python (i.e. contain no compiled extensions), but don’t natively support both Python 2 and 3.

To build the wheel:
"""
python setup.py bdist_wheel
"""

If your code supports both Python 2 and 3, but with different code (e.g., you use “2to3”) you can run setup.py bdist_wheel twice, once with Python 2 and once with Python 3. This will produce wheels for each version.

== Platform Wheels ==
Platform Wheels are wheels that are specific to a certain platform like Linux, macOS, or Windows, usually due to containing compiled extensions.

To build the wheel:

python setup.py bdist_wheel


#### Uploading your Project to PyPI

== Create an account ==
Note If you want to avoid entering your username and password when uploading, you can create a $HOME/.pypirc file with your username and password:
[pypi]
username = <username>
password = <password>

== Upload your distributions ==
Once you have an account you can upload your distributions to PyPI using twine. If this is your first time uploading a distribution for a new project, twine will handle registering the project.

twine upload dist/\*

You can see if your package has successfully uploaded by navigating to the URL https://pypi.org/project/<sampleproject> where sampleproject is the name of your project that you uploaded. It may take a minute or two for your project to appear on the site.



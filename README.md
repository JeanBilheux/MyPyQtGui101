PyQtGuiBase
======

Everything needed to start developping a PyQt application


Building
--------

Before doing the normal `python setup.py ...` things you must convert the
`designer/*.ui` files to `mygui/interfaces/*.py. 
This is done with
> python setup.py pyuic. 

To build the icons files
> python setup.py pyrcc


After that, all the normal
[setuptools](https://pythonhosted.org/setuptools/setuptools.html) magic applies.


[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](http://opensource.org/licenses/MIT)

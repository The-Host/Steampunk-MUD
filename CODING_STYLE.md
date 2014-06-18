Code Style
----------
All code submitted or committed to the project needs to follow
the guidelines outlined in Python PEP 8, which may be found at:

    http://www.python.org/dev/peps/pep-0008/

### A quick list of code style points

 * 4-space indentation, NO TABS!
 * Unix (``\n``) line endings.
 * CamelCase is only used for classes, nothing else.
 * All non-global variable names and all function names are to be
   lowercase, words separated by underscores. Variable names should
   always be more than two letters long.
 * Module-level global variables (only) are to be in CAPITAL letters.
 
In order to enforce this standard, you should be using a linter to 
automatically check this for you. [Pylint](http://www.pylint.org/) 
is one such tool. Many IDE's also have this feature, such as 
[Pycharm CE](http://www.jetbrains.com/pycharm/), in addition to many 
other code quality tools.


### Documentation

Modules, functions, classes and class methods should all start with 
at least one line of docstring summing up the function's purpose. 
Ideally also explain eventual arguments and caveats. Add comments 
where appropriate. Ideally, docstrings should follow Sphinx formatting
rules so documentation can be automatically generated from source.

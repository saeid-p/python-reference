# A module is an importable file containing definitions and statements.
# You can access its docstrings like this:
import modules

modules.__doc__ # This is the module docstring.
modules.welcome.__doc__ # This is the function docstring.



"""This is the module docstring."""

def welcome():
    """This is the function docstring."""
    return 'Welcome!'

# Specific functions of a module can be imported.
from modules import welcome
welcome()

# Modules can be aliased.
from modules import welcome as myWelcome
myWelcome()

# __name__ indicates te name of the currently running module.
print('__name__', __name__) # __main__

# If the module is inside a directory and needs to be detected by python,
# the directory should contain a file named "__init__.py"
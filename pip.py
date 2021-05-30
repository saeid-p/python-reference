# pip is a tool when you need to install any package available at the python package index (PyPI).
# pip is already installed if you're using Python 2 >= 2.7.9 or Python 3 >= 3.4.
# For computers running Linux or another native package manager, pip must often be manually installed.
# When both Python 2 and Python 3 installed, pip often refers to Python 2 and pip3 to Python 3.

#### Search packages ####
# pip search <query>

#### Installation ####

# pip install [package_name] # latest version of the package
# pip install [package_name]==x.x.x # specific version of the package
# pip install '[package_name]>=x.x.x' # minimum version of the package

# When your server is behind proxy, you can install package by using below command:
# pip --proxy http://<server address>:<port> install

#### Upgrading installed packages ####

# Get an overview of which of your installed packages have become outdated:
# pip list --outdated

# Upgrade a specific package:
# pip install [package_name] --upgrade

# Updating all outdated packages is not a standard functionality of pip.

#### Upgrading pip ####
# Linux/Max:
    # sudo pip install -U pip
# Windows:
    # py -m pip install -U pip
    # python -m pip install -U pip
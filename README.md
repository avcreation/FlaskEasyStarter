Flask Easy Starter v1.2
=======================

A python command line tool to easily start a flask project.
This script will create the architecture of the Flask project
and the configuration file. The default configuration use a SQLite
database.

# Requirements #

- python
- baker


# Installation #

    python setup.py install

# Usage #

    flask_starter.py startproject <your_project> [-V=<virtualenv_name]

If you want to use a virtual environment, user the -V option with the name of your virtual environment. ex:

    flask_starter.py startproject my_project -V=develop

## Optional ##
If you want Flask Easy Starter automatically install your required package,
create a file containing all the package name, each on a new line.

## Required ##
Run the flask_starter.py script with the `install_requirements` command (optionnaly with your requirements file).

If you want to use a virtual environment (here named 'develop'):

    source develop/bin/activate
    flask_starter.py install_requirements -R=<your_file>

Else, just do:

    flask_starter.py install_requirements -R=<your_file>

This will install all the required packages, starting with Flask and Flask-SQLAlchemy.

# TODO #
- Add default template

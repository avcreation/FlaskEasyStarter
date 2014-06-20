#!python
import baker
import os
import string
import random

def id_generator():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(64))

@baker.command
def startproject(name, V=""):
    """Creating a Flask project architecture and configuration.\n
    This use a SQLite database.

    <name>: The name of your flask project.\n
    -V=<string>: Create a virtual environment name <strong>.
    """

    # Try to create the project directory
    try:
        os.mkdir(name)
    except OSError:
        print "This directory already exist"
        return

    # Create all the subdirectories
    os.mkdir("%s/app" % name)
    os.mkdir("%s/app/templates" % name)
    os.mkdir("%s/app/static" % name)

    # Create and write the config file
    with open("%s/config.py" % name, "w") as config:
        config.write("CSRF_ENABLED = True\n")
        config.write("SECRET_KEY = '%s'\n" % id_generator() )
        config.write("\n")
        config.write("import os\n")
        config.write("basedir = os.path.abspath(os.path.dirname(__file__))\n")
        config.write("\n")
        config.write("SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')\n")
        config.write("SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')\n")

    # Write a script to create the database
    with open("%s/db_create.py" % name, "w") as db_create:
        db_create.write("# -*- coding:utf8 -*-\n")
        db_create.write("from config import SQLALCHEMY_DATABASE_URI\n")
        db_create.write("from app import db\n")
        db_create.write("\n")
        db_create.write("db.create_all()\n")

    # Write the runserver file
    with open("%s/runserver.py" % name, "w") as run:
        run.write("# -*- coding:utf8 -*-\n")
        run.write("from app import app\n")
        run.write("\n")
        run.write("app.run(debug = True)\n")

    # Write the __init__.py file
    with open("%s/app/__init__.py" % name, "w") as init:
        init.write("# -*- coding:utf8 -*-\n")
        init.write("from flask import Flask\n")
        init.write("from flask.ext.sqlalchemy import SQLAlchemy\n")
        init.write("\n")
        init.write("app = Flask(__name__)\n")
        init.write("app.config.from_object('config')\n")
        init.write("db = SQLAlchemy(app)\n")
        init.write("\n")
        init.write("from app import views, models\n")

    # Create the models file
    with open("%s/app/models.py" % name, "w") as models:
        models.write("# -*- coding:utf8 -*-\n")

    # Create the views file
    with open("%s/app/views.py" % name, "w") as views:
        views.write("# -*- coding:utf8 -*-\n")
        views.write("from . import app\n")
        views.write("# write your views here\n")

        views.write("@app.route(\"/\")\n")
        views.write("def index():\n")
        views.write("    return \"Hello World\"\n")

    warning = 0
    warning_text = ""

    # Create the virtual environment if you want one
    # This virtualenv need --system-site-packages because of baker
    # For requirements installation
    if V:
        virtualenv_install = os.system("pip install virtualenv")
        if virtualenv_install != 0:
            virtualenv_install = os.system("easy_install virtualenv")
            if virtualenv_install != 0:
                warning += 1
                warning_text += "- Can't install virtualenv. Please download it and run setup.py. Then, create your virtual environment manually.\n"
            else:
                os.system("virtualenv %s --system-site-packages" % V)
        else:
            os.system("virtualenv %s --system-site-packages" % V)

    # If there were warnings, print them
    if warning > 0:
        print "\nThere were %d warnings: " % warning
        print warning_text


@baker.command
def install_requirements(R=""):
    """Parse a requirement file if exist and install all the needed
    modules.

    <R>: File containing all the required modules. See example
    for further information.\n
    """

    warning = 0
    warning_text = ""

    # Install Flask (required)
    flask_install = os.system("pip install Flask")
    if flask_install != 0:
        warning += 1
        warning_text += "- Can't install Flask. Please download it and run setup.py.\n"

    # Install Flask-SQLAlchemy (required)
    flask_sqlal_install = os.system("pip install Flask-SQLAlchemy")
    if flask_install != 0:
        warning += 1
        warning_text +=  "- Can't install Flask-SQLAlchemy installation. Please download it and run setup.py.\n"

    # Install all your requirements
    if R:
        with open("%s" % R, 'r') as requirements:
            for l in requirements.readlines():
                flask_install = os.system("pip install %s" % l)
                if flask_install != 0:
                    warning += 1
                    warning_text += "- Can't install %s  Please download it and run setup.py.\n" % l

    # If there were warnings, print them
    if warning > 0:
        print "\nThere were %d warnings: " % warning
        print warning_text

baker.run()

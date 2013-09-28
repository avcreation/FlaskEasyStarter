from setuptools import setup

setup(
    name='FlaskEasyStarter',
    version='1.0',
    author='Alexandre Voiney',
    author_email='dev@avcreation.fr',
    packages=['flask-easy-starter'],
    scripts=['flask-easy-starter/flask_starter.py'],
    license='LICENSE.txt',
    description='Easily start a flask project.',
    long_description=open('README.md').read(),
    install_requires=[
        "baker >= 1.3",
    ],
)

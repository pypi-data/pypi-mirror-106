from setuptools import setup

setup(
    name='vivotek-focus',
    packages=["vivotekfocus"],
    version='0.1.0',
    author='Perzan',
    author_email='PerzanDevelopment@gmail.com',
    install_requires=[
        "requests~=2.25",
        "argparse~=1.4",
        "onetrick~=2.1",
        "keyring~=23.0"
    ]
)
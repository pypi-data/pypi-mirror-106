from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = ['game_sir_fixer']

setup(
    name="game_sir_fixer",

    version="0.0.1",

    packages=packages,
    install_requires=[
        'pygame',
        'pyvjoy',
    ],

    author="Grant miller",
    author_email="grant@grant-miller.com",
    description="A hacky workaround for the Game Sir wireless controller to interface with Dolphin Emulator",
    long_description=long_description,
    license="PSF",
    keywords="grant miller game sir dolphin emulator",
    url="https://github.com/GrantGMiller/game_sir_fixer",  # project home page, if any
    project_urls={
        "Source Code": "https://github.com/GrantGMiller/game_sir_fixer",
    }

)

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="RsCMPX_Base",
    version="4.0.7.9",
    description="CMX/CMP Base System Remote-control Module",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Rohde & Schwarz GmbH & Co. KG",
    copyright="Copyright © Rohde & Schwarz GmbH & Co. KG 2021",
    author_email="Customer.Support@rohde-schwarz.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=(find_packages(include=['RsCMPX_Base', 'RsCMPX_Base.*'])),
    install_requires=['PyVisa']
)
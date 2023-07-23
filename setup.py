# coding: utf-8
import pkg_resources
import setuptools
import os
from pathlib import Path

VERSION = "2.0.0"

file_path = os.path.join(Path('.'), "requirements.txt")
with open(file_path) as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

lib = "instrument.quote.source.client"

libs = [f"{lib}.{pkg}" for pkg in setuptools.find_packages(where="src")]
libs.append(lib)

setuptools.setup(
    name=lib,
    version=VERSION,
    description="Instrument quote source client",
    author_email="insonus.k@gmail.com",
    url="https://github.com/Instrument-Data-Source/Instrument-quote-data-source-client-python",
    keywords=["common"],
    install_requires=install_requires,
    packages=libs,
    package_dir={lib: 'src'},
    include_package_data=True,
    long_description="""\
    Client for service instrument quote source
    """
)
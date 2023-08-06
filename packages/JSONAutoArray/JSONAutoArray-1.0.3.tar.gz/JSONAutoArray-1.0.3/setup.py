"""
JSONAutoArray
-------------

Conveniently stream json-serializable python objects to an array in a file.

"""
import os
from setuptools import setup

try:
    from sphinx.setup_command import BuildDoc
    cmdclass = {"build_sphinx": BuildDoc}
except ModuleNotFoundError:
    pass

def read_text(path):
    """
    Read some text
    """
    with open(path, "r") as _fh:
        return _fh.read()

setup(
    name="JSONAutoArray",
    version="1.0.3",
    description="Write array to self-closing JSON file",
    long_description=read_text("README.md"),
    long_description_content_type="text/markdown",
    author="Doug Shawhan",
    author_email="doug.shawhan@gmail.com",
    maintainer="Doug Shawhan",
    maintainer_email="doug.shawhan@gmail.com",
    url="https://gitlab.com/doug.shawhan/json-autoarray",
    project_urls={
        "Bug Tracker": "https://gitlab.com/doug.shawhan/jsonautoarray/",
        "Source Code": "https://gitlab.com/doug.shawhan/jsonautoarray/master",
        "Development Version": "https://gitlab.com/doug.shawhan/jsonautoarray/dev",
        "Documentation": "https://jsonautoarray.readthedocs.io",
    },
    download_url="https://gitlab.com/doug.shawhan/json-autoarray",
    license=read_text("LICENSE.txt"),
    packages=["json_autoarray"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        ]
     )

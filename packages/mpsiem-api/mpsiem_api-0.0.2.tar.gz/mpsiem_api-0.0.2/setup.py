# --------------------------------------------------------------------------
# Copyright (c) Anton Kutepov. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------

"""Setup script for ptnad_api."""
import os
import re
import setuptools

def get_long_description():
    """
    Return the README.
    """
    long_description = ""    
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description += fh.read()
    return long_description

def get_version():
    """
    Return package version as listed in `__version__` in `__version__.py`.
    """
    with open("src/mpsiem_api/__version__.py", "r") as fd:
        v_match = re.search("__version__ = ['\"]([^'\"]+)['\"]", fd.read())
        __version__ = v_match.group(1) if v_match else "no version" 
    return __version__

setuptools.setup(
    name="mpsiem_api",
    version=get_version(),
    author="Kirill Kiryanov, Anton Kutepov",
    author_email="",
    description="Basic MaxPatrol SIEM API wrapper",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/aw350m33d/mpsiem_api",
    project_urls={
        "Bug Tracker": "https://github.com/aw350m33d/mpsiem_api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude=['tests']),
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'jinja2'
    ],
)

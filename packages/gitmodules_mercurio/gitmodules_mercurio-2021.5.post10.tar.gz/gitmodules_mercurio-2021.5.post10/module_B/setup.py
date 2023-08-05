#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
#import requirements as reqs
from collections import defaultdict
from setuptools import setup, find_namespace_packages
from version_module_B import __version__

# Extract the requirements from the deps file.
here = os.path.abspath(os.path.dirname(__file__))
microlib_name = "module_B"

with open(os.path.join(here, 'README.md')) as f:
    readme = f.read()


def get_install_requires(requirements_file: str):
    with open(os.path.join(here, requirements_file)) as f:
        req = [r.line for r in reqs.parse(f)]
    return req

setup(
    name=microlib_name,
    version=__version__,
    packages=find_namespace_packages(include=['module_B']),
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/maite828/module_B.git',  # Usa la URL del repositorio de GitHub
    download_url='https://github.com/maite828/modlue_B/archive/refs/heads/main.zip',
    description="Macrolib's description",
    license="MIT",
    #tests_require=get_install_requires('requirements_dev.txt'),
    python_requires=">=3.6",
    zip_safe=False,
    include_package_data=True,
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
from setuptools import setup, find_namespace_packages
from collections import defaultdict
from version import __version__


# Extract the requirements from the deps file.
here = os.path.abspath(os.path.dirname(__file__))
microlib_name = "gitmodules_mercurio"


def get_install_requires(requirements_file: str):
    with open(os.path.join(here, requirements_file)) as f:
        req = [r.line for r in reqs.parse(f)]
    return req


def get_extras_require():
    with open('requirements_extra.txt') as fp:
        extra_deps = defaultdict(set)
        for k in fp:
            if k.strip() and not k.startswith('#') and not k.startswith('-r'):
                tags = set()
                if '#' in k:
                    k, v = k.split('#')
                    tags.update(vv.strip() for vv in v.split(','))
                tags.add(re.split('[<=>]', k)[0])
                for t in tags:
                    extra_deps[t].add(k)
        extra_deps['all'] = set(vv for v in extra_deps.values() for vv in v)
    return extra_deps


setup(
    name=microlib_name,
    version=__version__,
    packages=find_namespace_packages(include=['module.*']),
    author="test analytics @example",
    author_email="echeverry.maite@gmail.com",
    url='https://github.com/maite828/gitmodules.git',  # Usa la URL del repositorio de GitHub
    download_url='https://github.com/maite828/gitmodules/archive/refs/heads/master.zip',
    description="Macrolib's description",
    license="MIT",
    extras_require=get_extras_require(),
    python_requires=">=3.6",
    zip_safe=False,
    include_package_data=True,
)

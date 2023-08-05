# -*- coding: utf-8 -*-

"""
TR0NZ0D Utils Library
~~~~~~~~~~~~~~~~~~~

Biblioteca criada para facilitar o acesso e utilização de ferramentas comuns.

:copyright: (c) 2021 TR0NZ0D
:license: MIT, see LICENSE for more details.

"""

__title__ = 'tr0nz0d'
__author__ = 'TR0NZ0D'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 TR0NZ0D'
__version__ = '0.0.1'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from collections import namedtuple
import logging

# Imports


VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel='Production/Stable', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
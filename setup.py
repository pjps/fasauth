#!/usr/bin/env python
#
# setup.py: script to install fasauth.py module.
#
# Author: P J P <pj.pandit@yahoo.co.in>
#
# This program is a free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the license, or(at your option)
# any later version. See http://www.gnu.org/copyleft/gpl.html for the full
# text of the license.
#

from distutils.core import setup

setup(name='askbot-plugin-authfas', version='0.1',
      description='Askbot plugin to facilitate FAS authentication.',
      author='P J P', author_email='pj.pandit@yahoo.co.in',
      url='http://github.com/pjps',
      py_modules = ['authfas'])

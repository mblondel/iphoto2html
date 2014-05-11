# -*- coding: utf-8 -*-

from distutils.core import setup

# Please run
# python setup.py install

setup(
    name = 'iphoto2html',
    description = 'Generate a static html gallery for your iPhoto library.',
    author = 'Mathieu Blondel',
    author_email = 'mathieu ÂT mblondel DÔT org',
    url = 'https://github.com/mblondel/iphoto2html',
    version = '0.1',
    license='Apache 2.0',
    packages = ['iphoto2html'],
    package_dir = {'iphoto2html': 'iphoto2html'},
    package_data = {'iphoto2html': ['data/*.*']},
    scripts = ['bin/iphoto2html'],

)

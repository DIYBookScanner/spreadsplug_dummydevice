#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    install_requires=['spreads'],
    name='spreadsplug_dummydevice',
    provides=['spreadsplug_dummydevice'],
    version='0.1',
    author='Johannes Baiter <johannes.baiter@gmail.com>, Matti Kariluoma <matti@kariluo.ma>',
    author_email='johannes.baiter@gmail.com',
    description='Spreads (http://github.com/DIYBookScanner/spreads http://spreads.readthedocs.org) plugin',
    license='MIT',
    classifiers=['Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX',
        'Topic :: Multimedia :: Graphics :: Capture',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'],
    keywords='spreads spreadsplugin',
    packages=['spreadsplug_dummydevice'],
    entry_points={u'spreadsplug.devices': [u'DummyDevice = spreadsplug_dummydevice.DummyDevicePlugin:DummyDevicePlugin']},
  )

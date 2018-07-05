#!/usr/bin/env python
'''
Setup for clicrud
'''
from setuptools import find_packages, setup

setup(name='clicrud',
      version='0.3.03-infranetlab',
      description='Brocade CLI CRUD Operations Library.',
      author='Brocade Communications Systems, Inc.',
      author_email='dgee@brocade.com',
      url='http://www.brocade.com/',
      packages=find_packages(),
      install_requires=["paramiko>=2.0.2", "jinja2"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking'
      ])

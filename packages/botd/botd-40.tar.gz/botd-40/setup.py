# This file is placed in the Public Domain.

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='botd',
    version='40',
    url='https://github.com/bthate/botd',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="24/7 channel daemon",
    long_description=read(),
    license='Public Domain',
    zip_safe=True,
    include_package_data=True,
    packages=["botd", "botl"],
    data_files=[('share/bot', ['files/botd.service', 'files/botd.8.md', 'files/botctl.8.md']),
                ('share/man/man8', ['files/botctl.8.gz', 'files/botd.8.gz'])],
    scripts=["bin/bot", "bin/botctl", "bin/botd"],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)

# This file is placed in the Public Domain.

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='genocide',
    version='32',
    url='https://github.com/bthate/genocide',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="OTP-CR-117/19 - otp.informationdesk@icc-cpi.int - https://genocide.rtfd.io",
    long_description=read(),
    license='Public Domain',
    packages=["gcd", "genocide"],
    zip_safe=True,
    scripts=["bin/genocide", "bin/genocided", "bin/genocidectl"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
 
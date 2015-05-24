import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

install_requires = [
    'pyramid',
    'jsonschema',
    'ramlfications',
]

tests_require = install_requires + [
    'pytest',
    'WebTest',
    'mock',
    'jsonschema',
]

setup(name='pyramid_raml',
    version='1.0.0',
    description='pyramid_raml',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    author='Igor Stroh',
    author_email='igor.stroh@rulim.de',
    url='http://github.com/jenner/pyramid_raml',
    keywords='web pyramid pylons api',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="pyramid_raml",
)
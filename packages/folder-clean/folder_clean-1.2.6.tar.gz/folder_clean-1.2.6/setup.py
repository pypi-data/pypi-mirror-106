from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'folder_clean', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='folder_clean',
    version=version['__version__'],
    description=('This library allows a user to specify which items (folders/files) that should be excluded from a folder clean.'),
    long_description=long_description,
    author='Kjell Klark',
    author_email='mrconter1@gmail.com',
    url='https://github.com/mrconter1/folder_clean',
    license='MPL-2.0',
    packages=['folder_clean'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )

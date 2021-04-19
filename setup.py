import io
import os
import re
from setuptools import setup, find_packages


def find_version():
    file_dir = os.path.dirname(__file__)
    with io.open(os.path.join(file_dir, 'auth0', '__init__.py')) as f:
        version = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read())
        if version:
            return version.group(1)
        else:
            raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='auth0-python',
    version=find_version(),
    description='Auth0 Python SDK',
    long_description=long_description,
    author='Auth0',
    author_email='support@auth0.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests>=2.14.0', 'pyjwt[crypto]>=1.7.1'],
    extras_require={'test': ['mock>=1.3.0', 'pre-commit']},
    python_requires='>=2.7, !=3.0.*, !=3.1.*',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/auth0/auth0-python',
)

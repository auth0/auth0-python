import os
import re

from setuptools import find_packages, setup


def find_version():
    file_dir = os.path.dirname(__file__)
    with open(os.path.join(file_dir, "auth0", "__init__.py")) as f:
        version = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read())
        if version:
            return version.group(1)
        else:
            raise RuntimeError("Unable to find version string.")


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="auth0-python",
    version=find_version(),
    description="Auth0 Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Auth0",
    author_email="support@auth0.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests>=2.14.0", "pyjwt[crypto]>=2.6.0"],
    extras_require={"test": ["coverage", "pre-commit"]},
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    url="https://github.com/auth0/auth0-python",
)

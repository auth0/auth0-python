#!/bin/bash

cd $(dirname ${0})
rm -rf auth0_python.egg-info/ build/ dist/
find . -name "*.pyc" -type f | xargs rm -f
rm -rf build
rm -rf dist
rm -rf .pytest_cache
rm -rf .tox
rm -rf .eggs
rm -rf docs/_build

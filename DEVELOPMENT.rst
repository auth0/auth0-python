Instructions to upload auth0-python to PyPI
===========================================

1) Create a ``.pypirc`` file in your home directory with the following
   contents (replace ``<username>`` and ``<password>`` with your PyPI
   credentials):

   .. code-block::

       [distutils]
       index-servers =
           pypi

       [pypi]
       repository: https://pypi.python.org/pypi
       username=<username>
       password=<password>

2) Bump the version number in ``auth0/__init__.py``.

3) Make sure you add changes to the `changelog <./CHANGELOG.md>`__.

4) Run the following command:

   .. code-block:: bash

       python3 setup.py sdist bdist_wheel --universal
       twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

   or do it using docker:

   .. code-block:: bash

       sh publish.sh

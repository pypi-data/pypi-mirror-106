# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_dataexporter']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2', 'openpyxl>=2.6']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'], 'docs': ['Sphinx>=3.5']}

setup_kwargs = {
    'name': 'django-dataexporter',
    'version': '1.0.0',
    'description': 'Extensible helper to export Django QuerySets and other data to CSV and Excel.',
    'long_description': "django-dataexporter\n===================\n\n.. image:: https://img.shields.io/pypi/v/django-dataexporter.svg\n   :target: https://pypi.org/project/django-dataexporter/\n   :alt: Latest Version\n\n.. image:: https://github.com/stephrdev/django-tapeforms/workflows/Test/badge.svg?branch=master\n   :target: https://github.com/stephrdev/django-tapeforms/actions?workflow=Test\n   :alt: CI Status\n\n.. image:: https://codecov.io/gh/lenarother/django-dataexporter/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/lenarother/django-dataexporter\n   :alt: Coverage Status\n\n.. image:: https://readthedocs.org/projects/django-dataexporter/badge/?version=latest\n   :target: https://django-dataexporter.readthedocs.io/en/stable/?badge=latest\n   :alt: Documentation Status\n\n\n*django-dataexporter* is a extensible helper to export Django QuerySets and other data to CSV and Excel.\n\n\nFeatures\n--------\n\n* Exporter class to generate CSV and Excel files out of QuerySets and other iterables.\n* Factory to generate Django ModelAdmin actions to trigger an export out of Django's famous admin interface.\n\n\nRequirements\n------------\n\ndjango-dataexporter supports Python 3 only and requires at least Django 2.\nIn addition, the Python package ``openpyxl`` needs to be installed.\n\n\nPrepare for development\n-----------------------\n\nA Python 3.6 interpreter is required in addition to poetry.\n\n.. code-block:: shell\n\n    $ poetry install\n\n\nNow you're ready to run the tests:\n\n.. code-block:: shell\n\n     $ poetry run pytest\n\n\nResources\n---------\n\n* `Documentation <https://django-dataexporter.readthedocs.io>`_\n* `Bug Tracker <https://github.com/lenarother/django-dataexporter/issues>`_\n* `Code <https://github.com/lenarother/django-dataexporter/>`_\n",
    'author': 'Stephan Jaekel',
    'author_email': 'steph@rdev.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lenarother/django-dataexporter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)

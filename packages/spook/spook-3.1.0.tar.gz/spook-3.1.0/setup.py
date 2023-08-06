# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spook']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=5.3,<6.0',
 'django>=1.11.0',
 'djangorestframework-jwt>=1.11.0,<2.0.0',
 'djangorestframework>=3.11.0,<4.0.0',
 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'spook',
    'version': '3.1.0',
    'description': 'Django Rest Framework library to interconnect external APIs',
    'long_description': "# Django Spook\n\n![PyPI](https://img.shields.io/pypi/v/spook?style=flat-square)\n[![codecov](https://codecov.io/gh/pablo-moreno/spook/branch/master/graph/badge.svg?token=6ZAHAHZG7Z)](https://codecov.io/gh/pablo-moreno/spook/)\n\nLibrary to interconnect multiple external HTTP APIs as Http Services\n\n## Installation\n\n```bash\npip install spook\n```\n\n## Usage\n\nDeclare a serializer class for your input validation\n\n```python\nfrom rest_framework import serializers\n\nclass MySerializer(serializers.ModelSerializer):\n    name = serializers.CharField()\n    age = serializers.IntegerField()\n    \n    class Meta:\n        fields = ('name', 'age', )\n```\n\nDeclare an InputValidator\n\n```python\nfrom spook.validators import InputValidator\n\n\nclass MyResourceInputValidator(InputValidator):\n    serializer_class = MySerializer\n```\n\n\nDeclare an API Resource class.\n\n```python\nfrom spook.resources import APIResource\n\n\nclass MyResource(APIResource):\n    api_url = 'https://my.external/api'\n    validator = MyResourceInputValidator\n```\n\nNow you can instance MyResource class and use the methods\n\n```python\nresource = MyResource()\n\n# List resources\nresource.list()\n\n# Retrieve a single resource\nresource.retrieve(pk=1)\n\n# Create resource\nresource.create({'name': 'Pablo', 'age': 28})\n\n# Update resource\nresource.update(pk=1, data={'name': 'Pablo Moreno'})\n\n# Delete resource\nresource.delete(pk=1)\n```\n\nThere are also some views available\n\n```python\nfrom spook.views import (\n    APIResourceRetrieveView, APIResourceListView, APIResourceCreateView, APIResourcePutView,\n    APIResourceRetrieveUpdateView, APIResourceRetrieveUpdateDestroyView, APIResourceListCreateView,\n)\n\n\nclass ListCreateProductResourceView(APIResourceListCreateView):\n    resource = ProductResource\n\n    def get_token(self, request):\n        return ''  # Wee need to override get_token()\n\n\nclass RetrieveUpdateDestroyProductResourceView(APIResourceRetrieveUpdateDestroyView):\n    resource = ProductResource\n\n    def get_token(self, request):\n        return ''\n```\n",
    'author': 'Pablo Moreno',
    'author_email': 'pablomoreno.inf@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)

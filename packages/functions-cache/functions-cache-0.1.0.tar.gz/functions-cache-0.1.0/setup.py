# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_cache',
 'functions_cache.engines',
 'functions_cache.engines.storage']

package_data = \
{'': ['*']}

extras_require = \
{'docs': ['docutils==0.16',
          'm2r2>=0.2,<0.3',
          'Sphinx==3.5.3',
          'sphinx-autodoc-typehints>=1.11,<2.0',
          'sphinx-copybutton>=0.3,<0.4',
          'sphinxcontrib-apidoc>=0.3,<0.4'],
 'engines': ['boto3>=1.15,<2.0', 'pymongo>=3.0,<4.0', 'redis>=3.0,<4.0']}

setup_kwargs = {
    'name': 'functions-cache',
    'version': '0.1.0',
    'description': 'cache functions output with auto refresh everytime you call it',
    'long_description': '# functions cache\n\nThis library is inspired by requests-cache <https://github.com/reclosedev/requests-cache> and the whole engines code has been copied and modified from there.\n\nthis library provide a decorator that can be used to decorate your functions to be cached.\n\nThe main feature that diffentiate this library is that it will auto refresh the cache in a background thread so your cache will be kept fresh.\n\n## Sample code\n```python\nfrom functions_cache import cache_it\nimport datetime\n\n\n\n@cache_it\ndef fab_cached(n):\n    if n < 2:\n        return n\n    else:\n        return fab_cached(n-2)+fab_cached(n-1)\n\nif __name__ == "__main__":\n    t1 = datetime.datetime.now()\n    print(fab_cached(100))\n    t2 = datetime.datetime.now()\n    print(t2-t1)\n    t3 = datetime.datetime.now()\n    print(fab_cached(100))\n    t4 = datetime.datetime.now()\n    print(t4-t3)\n    \n```\nand the output\n```\n354224848179261915075\n0:00:03.366472\n354224848179261915075\n0:00:00.014370\n```\n',
    'author': 'Baligh Hatem',
    'author_email': 'balighmehrez@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BalighMehrez/functions-cache',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

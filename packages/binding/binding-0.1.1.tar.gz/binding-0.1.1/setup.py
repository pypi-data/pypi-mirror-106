# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binding']

package_data = \
{'': ['*']}

install_requires = \
['forbiddenfruit>=0.1.4,<0.2.0']

setup_kwargs = {
    'name': 'binding',
    'version': '0.1.1',
    'description': 'Bindable properties for Python',
    'long_description': '# Binding\n\nBindable properties for Python.\n\n# Install\n\n```bash\npython3 -m pip install binding\n```\n\n# Usage\n\n```python\nimport binding\n\n...\n```\n\n# Dependencies\n\nTo archive this nice API we have to utilize `curse` from the [forbiddenfruit](https://pypi.org/project/forbiddenfruit/) package.\n',
    'author': 'Zauberzeug GmbH',
    'author_email': 'info@zauberzeug.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zauberzeug/binding',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

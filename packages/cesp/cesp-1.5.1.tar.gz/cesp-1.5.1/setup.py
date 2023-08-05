# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['cesp']
install_requires = \
['rich>=10.2.0,<11.0.0']

entry_points = \
{'console_scripts': ['cesp = cesp:main']}

setup_kwargs = {
    'name': 'cesp',
    'version': '1.5.1',
    'description': 'Converts blank space to underscore and other characters to avoid problems',
    'long_description': '# cesp\n\nConverts blank space to underscore and other characters to avoid problems\n\n## Getting Started\n\nThe easiest way to use **cesp** is to download the .exe file on [release pages](https://github.com/marcusbfs/cesp/releases).\nAfter downloading it, open CMD or PowerShell and execute\n\n```\ncesp.exe --help\n```\n\nto see the available options.\n\n## Contributing\n\nFeel free to contribute anyway you want to :)\n\n## Authors\n\n- **Marcus Bruno Fernandes Silva** - *marcusbfs@gmail.com*\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\n',
    'author': 'Marcus Bruno Fernandes Silva',
    'author_email': 'marcusbfs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

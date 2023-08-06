# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['et_dot']

package_data = \
{'': ['*'],
 'et_dot': ['cpp_dotc/CMakeLists.txt',
            'cpp_dotc/CMakeLists.txt',
            'cpp_dotc/CMakeLists.txt',
            'cpp_dotc/dotc.cpp',
            'cpp_dotc/dotc.cpp',
            'cpp_dotc/dotc.cpp',
            'cpp_dotc/dotc.rst',
            'cpp_dotc/dotc.rst',
            'cpp_dotc/dotc.rst',
            'f90_dotf/CMakeLists.txt',
            'f90_dotf/CMakeLists.txt',
            'f90_dotf/CMakeLists.txt',
            'f90_dotf/dotf.f90',
            'f90_dotf/dotf.f90',
            'f90_dotf/dotf.f90',
            'f90_dotf/dotf.rst',
            'f90_dotf/dotf.rst',
            'f90_dotf/dotf.rst']}

install_requires = \
['click>=7.0.0,<8.0.0']

entry_points = \
{'console_scripts': ['dotfiles = et_dot:cli_dotfiles.main']}

setup_kwargs = {
    'name': 'et-dot',
    'version': '0.0.1',
    'description': '<Enter a one-sentence description of this project here.>',
    'long_description': '======\nET-dot\n======\n\n\n\n<Enter a one-sentence description of this project here.>\n\n\n* Free software: MIT license\n* Documentation: https://ET-dot.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n',
    'author': 'Bert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/ET-dot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

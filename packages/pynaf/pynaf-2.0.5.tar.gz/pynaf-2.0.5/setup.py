# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynaf']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.6.3,<5.0.0']

setup_kwargs = {
    'name': 'pynaf',
    'version': '2.0.5',
    'description': 'Read and create NAF annotation Documents.',
    'long_description': 'pynaf\n=====\n\nPynaf provides  **a simple API for creating or reading NAF documents**.\n\nThe NAF (Natural language Annotation Format) is **an XML markup language that contains several layers of linguistic annotation**. It is used in **Natural Language Processing tools** like [IXA Pipes] (http://ixa2.si.ehu.es/ixa-pipes/) or [Corefgraph](https://bitbucket.org/Josu/corefgraph).\n\n**More information** about NAF in the  following [link ](https://github.com/newsreader/NAF).\n\n\nInstall from Pip(Recommended)\n----\nInstall pinaf directly from Pypi repositories\n\n    Pip install pynaf\n\n\nInstall from repository\n-----\n\nInstall pynaf using this command (no need to clone the repository):\n\n    pip install --upgrade --user git+https://github.com/josubg/pynaf.git\n',
    'author': 'Rodrigo Agerri',
    'author_email': 'rodrigo.agerri@ehu.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/josubg/pynaf/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

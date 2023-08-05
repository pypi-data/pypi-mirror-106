# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nerm']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.0', 'commonmark>=0.9.0', 'tomlkit>=0.7.0']

entry_points = \
{'console_scripts': ['nerm = nerm.nerm:main_cli']}

setup_kwargs = {
    'name': 'nerm',
    'version': '0.1.0',
    'description': 'Nerm - No Effort Requirements Management',
    'long_description': 'Nerm - No Effort Requirements Management\n========================================\n\nNerm is a tool that automatically updates Markdown-formatted text files to track\nproject requirements. For each requirement, nerm will list any files and git commits\nthat mention it. User can specify rules for satisfying requirements, such as\neach requirement must have an implementation and a test, and nerm will check that.\n\nCheck out the [example requirements document](requirements/nerm.md).\n\nCore principles\n---------------\n\n1. Requirement management tool should reduce effort, not add it.\n   Nerm does not require boilerplate or complex formatting for the input files.\n\n2. Information in one place: Instead of separate reports, the cross-references\n   are added directly in the requirements document.\n\n\nInstallation\n------------\n\nEasiest way to install nerm is using Python package manager `pip`:\n\n    pip install nerm\n\nIf `pip` on your system is Python 2.x, use `pip3` instead.\n\nOnce installed, you can test it works by running `nerm --help`.\n\nGetting started\n---------------\n<!--- [DR-Readme] and [DR-Example] documented here --->\n\nCreate your requirements document as a Markdown formatted file.\nFor each requirement, add a heading that starts with a requirement tag in format `[TAG]`:\n\n    [ExampleReq] Example requirement\n    --------------------------------\n    This is my example requirement.\n\nWhen you add code or other files related to the requirement, use the tag in e.g. comments:\n\n    myfunction() {\n        // This function implements [ExampleReq]\n    }\n\nNow when you run `nerm -u`, the requirement document will get updated with a list of cross-references for each discovered tag.\n\nTo customize the functionality, you can create a `Nermfile.toml`.\nSee [full documentation](docs/Nermfile.md) for the available options.\n\nAlso check out [the requirements document](requirements/nerm.md) and [Nermfile](Nermfile.toml) of this project itself.',
    'author': 'Petteri Aimonen',
    'author_email': 'jpa@git.mail.kapsi.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)

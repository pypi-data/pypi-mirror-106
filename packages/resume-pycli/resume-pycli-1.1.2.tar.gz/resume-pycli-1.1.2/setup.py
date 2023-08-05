# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['resume_pycli']

package_data = \
{'': ['*'], 'resume_pycli': ['themes/base/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'click>=8.0.0,<9.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'pdfkit>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['resume = resume_pycli.script:cli',
                     'resumepy = resume_pycli.script:cli']}

setup_kwargs = {
    'name': 'resume-pycli',
    'version': '1.1.2',
    'description': 'CLI tool to easily setup a new resume',
    'long_description': '# resume-pycli\n\n[![builds.sr.ht status](https://builds.sr.ht/~nka/resume-pycli.svg)](https://builds.sr.ht/~nka/resume-pycli?)\n[![PyPI version](https://badge.fury.io/py/resume-pycli.svg)](https://badge.fury.io/py/resume-pycli)\n\nCLI tool to build a beautiful resume from a [JSON Resume](https://jsonresume.org/) file.\n\nThis is a Python port of [resume-cli](https://github.com/jsonresume/resume-cli).\n\n## Installation\n\nWith [pipx](https://pipxproject.github.io/pipx/):\n\n```\npipx install resume-pycli\n```\n\nWith [brew](https://brew.sh/):\n\n```\nbrew install nikaro/tap/resume-pycli\n```\n\nOn ArchLinux from the [AUR](https://aur.archlinux.org/packages/resume-pycli/):\n\n```\nyay -S resume-pycli\n\n# or without yay\ngit clone https://aur.archlinux.org/resume-pycli.git\ncd resume-pycli/\nmakepkg -si\n```\n\n\n## Usage\n\n```\nUsage: resume [OPTIONS] COMMAND [ARGS]...\n\n  CLI tool to easily setup a new resume.\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  export    Export to HTML and PDF.\n  init      Initialize a resume.json file.\n  serve     Serve resume.\n  validate  Validate resume\'s schema.\n```\n\n## Themes\n\nYou can put your theme in `themes/<name>` next to your `resume.json` file. It uses [Jinja2](https://jinja2docs.readthedocs.io/en/stable/) as templating engine. Take a look at the [small demo](https://git.sr.ht/~nka/resume-pycli/tree/main/item/src/resume_pycli/themes/base/) that you can take as example to write your own.\n\nIt is not compatible with ["official" community themes](https://jsonresume.org/themes/) and at the moment i have not included a beautiful one.\n',
    'author': 'Nicolas Karolak',
    'author_email': 'nicolas@karolak.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://sr.ht/~nka/resume-pycli',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

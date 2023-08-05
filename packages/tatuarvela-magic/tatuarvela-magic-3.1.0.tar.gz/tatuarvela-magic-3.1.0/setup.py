# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magic', 'magic.shared']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0,<9.0.0', 'fastjsonschema>=2.15.0,<3.0.0']

entry_points = \
{'console_scripts': ['magic = magic:main']}

setup_kwargs = {
    'name': 'tatuarvela-magic',
    'version': '3.1.0',
    'description': 'A tool for simplifying repeated command line tasks',
    'long_description': '# ![Magic icon](./icon.png?raw=true "Magic icon") Magic\n\n[![Repository](https://img.shields.io/badge/repository-gray.svg?logo=github)](https://github.com/TatuArvela/Magic)\n[![GitHub issues](https://img.shields.io/github/issues/TatuArvela/Magic)](https://github.com/TatuArvela/Magic/issues)\n[![Pipeline status](https://github.com/TatuArvela/Magic/actions/workflows/verify.yml/badge.svg?event=push)](https://github.com/TatuArvela/Magic/actions/workflows/verify.yml)\n[![PyPI](https://img.shields.io/pypi/v/tatuarvela-magic)](https://pypi.org/project/tatuarvela-magic/)\n[![License](https://img.shields.io/github/license/TatuArvela/Magic)](https://github.com/TatuArvela/Magic/blob/master/LICENSE)\n[![Created at Nitor](https://img.shields.io/badge/created%20at-Nitor-informational.svg)](https://nitor.com/)\n\nMagic is a tool for wrapping repeated command line tasks into simple scripts.\n\n* A sequence of console commands is saved as a **spell**\n* Spells are written into the **spellbook** file (`~/.spellbook.json`)\n* Each spell can be called with one or several **magic words**  \n  e.g. `magic build-app` and `magic ba`\n* Spells can have **arguments** passed to them  \n  e.g. `magic say abra kadabra`\n* Magic can report the execution time of spells, which may be useful for longer\n  operations\n\n## Installation\n\nMagic is designed for macOS and common Linux distributions using Bash or Zsh.\nWindows is not supported.\n\nMagic requires Python 3.9, and can be installed using pip:\n\n```console\npython3 -m pip install tatuarvela-magic\n```\n\nSee also: [Development installation](#development-installation)\n\n## Usage\n\n```console\n$ magic\n✨ Magic v3.1.0 © 2021 Tatu Arvela\nA tool for simplifying repeated command line tasks\n\nUsage: magic [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -h, --help  Show this message and exit.\n\nCommands:\n  add      Add spell to spellbook\n  e        Example echo spell with arguments \'$a0\' and \'$a1\'\n  edit     Open spellbook in editor\n  example  Example echo spell with arguments \'$a0\' and \'$a1\'\n```\n\nEditing the spellbook is currently done with an external editor (**Visual Studio\nCode** by default).\n\n### Spell options\n\n```console\n$ magic example --help\nUsage: magic example [OPTIONS]\n\n  Example echo spell with arguments \'$a0\' and \'$a1\'\n\nOptions:\n  -d, --delete  Delete this spell.\n  -s, --show    Show details of this spell.\n  -h, --help    Show this message and exit.\n```\n\nOther options are interpreted as arguments for spells.\n\n### Spell arguments\n\nSpells can have an array of arguments, which are populated according to their\nindex. Excessive usage is considered to be an anti-pattern, it is recommended to\ncreate separate spells instead.\n\nExample:\n\n```json\n{\n  "description": "Example echo spell with arguments \'$a0\' and \'$a1\'",\n  "magicWords": [\n    "e",\n    "example"\n  ],\n  "commands": [\n    "echo $a0",\n    "echo $a1"\n  ],\n  "argumentCount": 2\n}\n```\n\n```console\n$ magic example cat dog\n✨ Example echo spell with arguments \'cat\' and \'dog\'\ncat\ndog\n✅ 23:46:43 | ⏱ 0:00:00\n```\n\n#### Advanced usage: Empty arguments\n\nArgument are handled as an ordered array. If necessary, it is possible to make an argument an empty string: `\'\'`.\n\n## Development\n\n### Development installation\n\n* Supported operating systems: macOS (untested on Linux)\n* Requirements: Python 3, Poetry\n\n1. Clone the Git repository somewhere and navigate to it on the command line\n\n   ```bash\n   git clone https://github.com/TatuArvela/Magic.git\n   cd Magic\n   ```\n\n2. Install `magic` and its dependencies to a virtual env\n\n   ```bash\n   poetry install\n   ```\n\n3. Verify that `magic` works\n\n   ```bash\n   poetry run magic\n   ```\n\n4. Register `magic` to your `PATH`\n\n    ```bash\n    python -m write_path\n    ```\n\nWhen developing the tool, you should use the `magic` module directly\nwith `python -m magic`.\n\nAfter successful changes, you need to run `poetry install` again to update the\nversion in your `PATH`.\n\n### Code quality tools\n\nMagic uses `isort`, `black` and `flake8` as its code quality tools. They are\nexecuted automatically with `pre-commit` and can also be executed with the\nincluded lint script:\n\n```bash\npython -m lint\n```\n\n### TODO\n\n#### For 3.X.X releases\n\n* Add `pytest`, `snapshottest`, `coverage.py`\n',
    'author': 'Tatu Arvela',
    'author_email': 'tatu.arvela@nitor.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TatuArvela/Magic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

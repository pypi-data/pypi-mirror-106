# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['setup_headers']

package_data = \
{'': ['*']}

install_requires = \
['Cerberus>=1.3.4,<2.0.0', 'PyYAML>=5.4.1,<6.0.0', 'glom>=20.11.0,<21.0.0']

extras_require = \
{'coverage': ['pytest>=6.2.2,<7.0.0',
              'coverage>=5.4,<6.0',
              'PyHamcrest>=2.0.2,<3.0.0'],
 'interactive-dev': ['pre-commit>=2.10.1,<3.0.0',
                     'autopep8>=1.5.5,<2.0.0',
                     'isort>=5.7.0,<6.0.0',
                     'flake8>=3.8.4,<4.0.0',
                     'rope>=0.18.0,<0.19.0'],
 'tests': ['pytest>=6.2.2,<7.0.0',
           'PyHamcrest>=2.0.2,<3.0.0',
           'behave>=1.2.6,<2.0.0']}

entry_points = \
{'console_scripts': ['adjust-license-header = setup_headers.main:main']}

setup_kwargs = {
    'name': 'jfaleiro.setup-headers',
    'version': '0.0.3',
    'description': 'Sets a standard header in all source files.',
    'long_description': '# setup_headers\n\nSets a standard header in all source files. Searches a project directory tree finding all files matching a sequence of `glob` patterns (e.g. `**/*.py`,`*.cfg`,`**/config/*.yml`), and replaces any comments on the beginning of the file by lines from a header file, preceded by a comment marker (a prefix).\n\nThe substitution does not apply to "hashbangs" (anything started by `#!`). These will be kept where they were originally.\n\nSee _LICENSE_ for important licensing information.\n\n## Installation\n\nYou can use any `pip` compliant tool:\n\n```bash\npip install jfaleiro.setup_headers\n```\n\nOr something like `poetry`:\n\n```bash\npoetry add jfaleiro.setup_headers\n```\n\nIf you use `pre-commit` a pip or poetry installation is not required. See below.\n\n## Configuration\n\nAs of release `0.0.5`, with the migration to poetry, `distutils.commands` is no longer supported.\n\nSince the use of poetry plugins [requires a dependency on poetry](https://github.com/python-poetry/poetry/blob/master/docs/docs/plugins.md), a massive toolset, we moved away from a build tool extension altogether. We will reconsider when and if Python\'s strugle with its dependency hell improves.\n\nThe configuration of where license headers will be added is given in a file named `headers.yaml` by default:\n\n```yaml\nheader: HEADER\nprefixes:\n  - prefix: "#"\n    globs: [\n    "setup_headers/**/*.py",\n    "test/**/*.py",\n    ".devcontainer/Dockerfile",\n    "Makefile"]\n  - prefix: "##"\n    globs:\n    - "*.yml"\n    - "*.yaml"\n  - prefix: "//"\n    globs:\n    - ".devcontainer/devcontainer.json"\n  - prefix: ";"\n    globs: [\n        setup.cfg,\n        tox.ini\n      ]\n```\n\nEach `prefix` is a recognized comment character(s) on the beginning of each line in the header. Globs are a `pathlib.glob()` pattern. Only relative patterns are allowed.\n\nThe `**/*` comes from Python\'s Pathlib and indicates all matches under that directory. The pattern `**` will match only sub-directories, what is probably [not what you want](https://stackoverflow.com/questions/49047402/python-3-6-glob-include-hidden-files-and-folders).\n\nCreate a file matching the name on the `header` with what you want to be inserted on the beginning of all files that match the `globs` pattern, something like:\n\n```text\n     my_awesome_project - Does something awesome\n\n     Copyright (C) 2019 Joe Doe.\n\n     This program is not free. You should pay lots of money to use it.\n     Contact me for my paypal account.\n\n     You should have received a copy of My Proprietary License\n     along with this program.  If not, see <http://joe.doe/licenses/>.\n\n```\n\n## Use\n\n### Setuptools Command\n\nAs of release `0.0.5`, with the migration to poetry, `distutils.commands` is no longer supported. See above.\n\n\n### Command Line\n\nYou can also use the CLI for any projects that do not care or rely on `setuptools`:\n\n```\n$ adjust-license-header --help\nusage: adjust-license-header [-h] [--config CONFIG] [--dry-run] [--prefix-mandatory] [files [files ...]]\n\npositional arguments:\n  files               process only files in the list (default: None)\n\noptional arguments:\n  -h, --help          show this help message and exit\n  --config CONFIG     name of the YAML config file (default: headers.yaml)\n  --dry-run           don\'t apply any changes (default: False)\n  --prefix-mandatory  failure if file is not associated to a prefix (default: False\n```\n\n### Pre-Commit\n\nFinally, the preferred way, you can keep license notices up to date at `git` commit time. Just add a `.pre-commit-config.yaml` to your project root:\n\n```yaml\n# See https://pre-commit.com for more information on pre-commit\n# See https://pre-commit.com/hooks.html for more hooks\n\nrepos:\n-   repo: https://gitlab.com/jfaleiro.open/setup_headers\n    rev: 0.0.2\n    hooks:\n    - id: adjust-license-header\n```\n\nIf you use `pre-commit` a pip or poetry installation is not required.\n',
    'author': 'Jorge M Faleiro Jr',
    'author_email': 'j@falei.ro',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/jfaleiro.open/setup_headers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)

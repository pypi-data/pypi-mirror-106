# setup_headers

Sets a standard header in all source files. Searches a project directory tree finding all files matching a sequence of `glob` patterns (e.g. `**/*.py`,`*.cfg`,`**/config/*.yml`), and replaces any comments on the beginning of the file by lines from a header file, preceded by a comment marker (a prefix).

The substitution does not apply to "hashbangs" (anything started by `#!`). These will be kept where they were originally.

See _LICENSE_ for important licensing information.

## Installation

You can use any `pip` compliant tool:

```bash
pip install jfaleiro.setup_headers
```

Or something like `poetry`:

```bash
poetry add jfaleiro.setup_headers
```

If you use `pre-commit` a pip or poetry installation is not required. See below.

## Configuration

As of release `0.0.5`, with the migration to poetry, `distutils.commands` is no longer supported.

Since the use of poetry plugins [requires a dependency on poetry](https://github.com/python-poetry/poetry/blob/master/docs/docs/plugins.md), a massive toolset, we moved away from a build tool extension altogether. We will reconsider when and if Python's strugle with its dependency hell improves.

The configuration of where license headers will be added is given in a file named `headers.yaml` by default:

```yaml
header: HEADER
prefixes:
  - prefix: "#"
    globs: [
    "setup_headers/**/*.py",
    "test/**/*.py",
    ".devcontainer/Dockerfile",
    "Makefile"]
  - prefix: "##"
    globs:
    - "*.yml"
    - "*.yaml"
  - prefix: "//"
    globs:
    - ".devcontainer/devcontainer.json"
  - prefix: ";"
    globs: [
        setup.cfg,
        tox.ini
      ]
```

Each `prefix` is a recognized comment character(s) on the beginning of each line in the header. Globs are a `pathlib.glob()` pattern. Only relative patterns are allowed.

The `**/*` comes from Python's Pathlib and indicates all matches under that directory. The pattern `**` will match only sub-directories, what is probably [not what you want](https://stackoverflow.com/questions/49047402/python-3-6-glob-include-hidden-files-and-folders).

Create a file matching the name on the `header` with what you want to be inserted on the beginning of all files that match the `globs` pattern, something like:

```text
     my_awesome_project - Does something awesome

     Copyright (C) 2019 Joe Doe.

     This program is not free. You should pay lots of money to use it.
     Contact me for my paypal account.

     You should have received a copy of My Proprietary License
     along with this program.  If not, see <http://joe.doe/licenses/>.

```

## Use

### Setuptools Command

As of release `0.0.5`, with the migration to poetry, `distutils.commands` is no longer supported. See above.


### Command Line

You can also use the CLI for any projects that do not care or rely on `setuptools`:

```
$ adjust-license-header --help
usage: adjust-license-header [-h] [--config CONFIG] [--dry-run] [--prefix-mandatory] [files [files ...]]

positional arguments:
  files               process only files in the list (default: None)

optional arguments:
  -h, --help          show this help message and exit
  --config CONFIG     name of the YAML config file (default: headers.yaml)
  --dry-run           don't apply any changes (default: False)
  --prefix-mandatory  failure if file is not associated to a prefix (default: False
```

### Pre-Commit

Finally, the preferred way, you can keep license notices up to date at `git` commit time. Just add a `.pre-commit-config.yaml` to your project root:

```yaml
# See https://pre-commit.com for more information on pre-commit
# See https://pre-commit.com/hooks.html for more hooks

repos:
-   repo: https://gitlab.com/jfaleiro.open/setup_headers
    rev: 0.0.2
    hooks:
    - id: adjust-license-header
```

If you use `pre-commit` a pip or poetry installation is not required.

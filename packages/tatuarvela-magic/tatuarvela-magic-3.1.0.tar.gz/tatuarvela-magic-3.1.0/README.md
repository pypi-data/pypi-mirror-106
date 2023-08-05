# ![Magic icon](./icon.png?raw=true "Magic icon") Magic

[![Repository](https://img.shields.io/badge/repository-gray.svg?logo=github)](https://github.com/TatuArvela/Magic)
[![GitHub issues](https://img.shields.io/github/issues/TatuArvela/Magic)](https://github.com/TatuArvela/Magic/issues)
[![Pipeline status](https://github.com/TatuArvela/Magic/actions/workflows/verify.yml/badge.svg?event=push)](https://github.com/TatuArvela/Magic/actions/workflows/verify.yml)
[![PyPI](https://img.shields.io/pypi/v/tatuarvela-magic)](https://pypi.org/project/tatuarvela-magic/)
[![License](https://img.shields.io/github/license/TatuArvela/Magic)](https://github.com/TatuArvela/Magic/blob/master/LICENSE)
[![Created at Nitor](https://img.shields.io/badge/created%20at-Nitor-informational.svg)](https://nitor.com/)

Magic is a tool for wrapping repeated command line tasks into simple scripts.

* A sequence of console commands is saved as a **spell**
* Spells are written into the **spellbook** file (`~/.spellbook.json`)
* Each spell can be called with one or several **magic words**  
  e.g. `magic build-app` and `magic ba`
* Spells can have **arguments** passed to them  
  e.g. `magic say abra kadabra`
* Magic can report the execution time of spells, which may be useful for longer
  operations

## Installation

Magic is designed for macOS and common Linux distributions using Bash or Zsh.
Windows is not supported.

Magic requires Python 3.9, and can be installed using pip:

```console
python3 -m pip install tatuarvela-magic
```

See also: [Development installation](#development-installation)

## Usage

```console
$ magic
✨ Magic v3.1.0 © 2021 Tatu Arvela
A tool for simplifying repeated command line tasks

Usage: magic [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  add      Add spell to spellbook
  e        Example echo spell with arguments '$a0' and '$a1'
  edit     Open spellbook in editor
  example  Example echo spell with arguments '$a0' and '$a1'
```

Editing the spellbook is currently done with an external editor (**Visual Studio
Code** by default).

### Spell options

```console
$ magic example --help
Usage: magic example [OPTIONS]

  Example echo spell with arguments '$a0' and '$a1'

Options:
  -d, --delete  Delete this spell.
  -s, --show    Show details of this spell.
  -h, --help    Show this message and exit.
```

Other options are interpreted as arguments for spells.

### Spell arguments

Spells can have an array of arguments, which are populated according to their
index. Excessive usage is considered to be an anti-pattern, it is recommended to
create separate spells instead.

Example:

```json
{
  "description": "Example echo spell with arguments '$a0' and '$a1'",
  "magicWords": [
    "e",
    "example"
  ],
  "commands": [
    "echo $a0",
    "echo $a1"
  ],
  "argumentCount": 2
}
```

```console
$ magic example cat dog
✨ Example echo spell with arguments 'cat' and 'dog'
cat
dog
✅ 23:46:43 | ⏱ 0:00:00
```

#### Advanced usage: Empty arguments

Argument are handled as an ordered array. If necessary, it is possible to make an argument an empty string: `''`.

## Development

### Development installation

* Supported operating systems: macOS (untested on Linux)
* Requirements: Python 3, Poetry

1. Clone the Git repository somewhere and navigate to it on the command line

   ```bash
   git clone https://github.com/TatuArvela/Magic.git
   cd Magic
   ```

2. Install `magic` and its dependencies to a virtual env

   ```bash
   poetry install
   ```

3. Verify that `magic` works

   ```bash
   poetry run magic
   ```

4. Register `magic` to your `PATH`

    ```bash
    python -m write_path
    ```

When developing the tool, you should use the `magic` module directly
with `python -m magic`.

After successful changes, you need to run `poetry install` again to update the
version in your `PATH`.

### Code quality tools

Magic uses `isort`, `black` and `flake8` as its code quality tools. They are
executed automatically with `pre-commit` and can also be executed with the
included lint script:

```bash
python -m lint
```

### TODO

#### For 3.X.X releases

* Add `pytest`, `snapshottest`, `coverage.py`

# datasette-gfm

[![PyPI](https://img.shields.io/pypi/v/datasette-gfm.svg)](https://pypi.org/project/datasette-gfm/)
[![Changelog](https://img.shields.io/github/v/release/postman-open-technologies/datasette-gfm?include_prereleases&label=changelog)](https://github.com/postman-open-technologies/datasette-gfm/releases)
[![Tests](https://github.com/postman-open-technologies/datasette-gfm/workflows/Test/badge.svg)](https://github.com/postman-open-technologies/datasette-gfm/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/postman-open-technologies/datasette-gfm/blob/main/LICENSE)

Export Datasette records as GitHub flavoured markdown

## Installation

Install this plugin in the same environment as Datasette.

    $ datasette install datasette-gfm

## Usage

Having installed this plugin, every table and query will gain a new `.md` export link.

You can also construct these URLs directly: `/dbname/tablename.md`

## Demo

TBD

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-gfm
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest

## Thanks

This plugin is very heavily based on [datasette-yaml](https://github.com/simonw/datasette-yaml) by Simon Willison.


# Owl Utils

> Common set of utilities when building a web app

[![PyPI Version][pypi-image]][pypi-url]

Parsing functions:

- safeint
- safeintorzero
- safeintorbignumber
- safefloat
- jsonb_date_to_str
- pretty_json
- onewhite
- join_strings_if_not_null
- get_full_name
- get_exception_traceback

## Installation
```shell
pip install owlutils
```

## Usage

```python
>>> from owlutils import parsing
>>> parsing.safeint("123")
```

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/owlutils
[pypi-url]: https://pypi.org/project/owlutils/

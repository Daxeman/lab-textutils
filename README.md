# textutils

# lab-textutils

![CI](https://github.com/Daxeman/lab-textutils/actions/workflows/ci.yml/badge.svg)


A small Python library for text processing. Provides utilities for:

- **slugify** — converting text strings into URL-safe slugs
- **password** — evaluating password strength
- **stats** — analysing basic text statistics

This project has tests but no CI pipeline. That's your job.

---

## Project structure

```
lab-textutils/
├── src/
│   └── textutils/
│       ├── __init__.py
│       ├── slugify.py
│       ├── password.py
│       └── stats.py
├── tests/
│   ├── __init__.py
│   ├── test_slugify.py
│   ├── test_password.py
│   └── test_stats.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Getting started

Create a virtual environment and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the tests

```
pytest
pytest -v
pytest --cov=textutils --cov-report=term-missing
```

## Quick usage example

```python
from textutils import slugify, check_strength, summarize

print(slugify("Hello World!"))
# hello-world

print(check_strength("abc"))
# svagt

print(summarize("Two sentences here. And one more!"))
# {'ord': 6, 'meningar': 2, 'tecken': 34, 'genomsnittlig_ordlangd': 4.83}
```

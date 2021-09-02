# Overview

How to implement the factory pattern properly in python.
https://realpython.com/factory-method-python/

Factory Method is a creational design pattern used to create concrete implementations of a common interface.

It separates the process of creating an object from the code that depends on the interface of the object.


## Development Setup

Run the following in cmd to set up the local environment:

```
python -m venv venv
.\venv\scripts\activate.ps1
python -m pip install --upgrade pip
pip install -r dev_requirements.txt
pip install -r requirements.txt
```

To install the cli interactively as you develop:
```
pip install -e .
```

## Semantic Versioning

Note that builds will automatically semantic version. Use git tags for a valid PEP-440 release.

## Build

Run the following to build:

```
python setup.py sdist bdist_wheel
```





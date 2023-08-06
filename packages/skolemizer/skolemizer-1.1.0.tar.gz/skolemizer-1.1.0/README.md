![Tests](https://github.com/Informasjonsforvaltning/skolemizer/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/Informasjonsforvaltning/skolemizer/branch/main/graph/badge.svg)](https://codecov.io/gh/Informasjonsforvaltning/skolemizer)
[![PyPI](https://img.shields.io/pypi/v/skolemizer.svg)](https://pypi.org/project/skolemizer/)
[![Read the Docs](https://readthedocs.org/projects/skolemizer/badge/)](https://skolemizer.readthedocs.io/)
# skolemizer
A library with utils for performing Skolemization on blank nodes (RDF)

W3C has a short intro to skolemization here:
https://www.w3.org/2011/rdf-wg/wiki/Skolemisation

## Development
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [pipx](https://github.com/pipxproject/pipx) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://github.com/cjolowicz/nox-poetry)

```
% pipx install poetry==1.1.6
% pipx install nox==2020.12.31
% pipx inject nox nox-poetry
```
### Install
```
% git clone https://github.com/Informasjonsforvaltning/skolemizer.git
% cd skolemizer
% pyenv install 3.9.4
% pyenv local 3.9.4
% poetry install
```
### Getting started
Remember before starting to always set the baseurl for skolemization, according to your organizations url.
This can be done by setting the environment variable skolemizer_baseurl on your operation system.
It can also e.g be done run time through Python's os package:
```
os.environ[Skolemizer.baseurl_key] = "https://www.someorganiztion.somedomain/"
```
If not set Skolemizer will use "http://example.com/" as base url.
In order to invoke the skolemizer for ensuring identifier of rdf-nodes simply add
```
from skolemizer import Skolemizer
```
and then before rdf-serialization of a class:
```
        if not getattr(self, "identifier", None):
            self.identifier = Skolemizer.add_skolemization()
```
There should also be a skolemization check performed when serializing object properties.
When creating unit tests of skolemized rdf nodes a uuid will be applied as a substring of the complete skolemization.
Therefore, in order to create stable unit tests one can use the testsutils in order to mock a stable skolemization.

E.g pytest-mock's MockFixture permits mocking of the skolemizer:
```
    from pytest_mock import MockFixture
    from skolemizer import skolemization

    catalog = Catalog()

    mocker.patch(
        "skolemizer.Skolemizer.add_skolemization",
        return_value=skolemization
    )
```
which outputs e.g:
```
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix dcat: <http://www.w3.org/ns/dcat#> .

        <http://wwww.digdir.no/.well-known/skolem/284db4d2-80c2-11eb-82c3-83e80baa2f94>
         a dcat:Catalog  .

```
### Run all sessions
```
% nox
```
### Run all tests with coverage reporting
```
% nox -rs tests
```
### Debugging
You can enter into [Pdb](https://docs.python.org/3/library/pdb.html) by passing `--pdb` to pytest:
```
nox -rs tests -- --pdb
```
You can set breakpoints directly in code by using the function `breakpoint()`.

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['skolemizer']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.5.0,<2.0.0']}

setup_kwargs = {
    'name': 'skolemizer',
    'version': '1.1.0',
    'description': 'A library with utils for performing Skolemization on blank nodes (RDF)',
    'long_description': '![Tests](https://github.com/Informasjonsforvaltning/skolemizer/workflows/Tests/badge.svg)\n[![codecov](https://codecov.io/gh/Informasjonsforvaltning/skolemizer/branch/main/graph/badge.svg)](https://codecov.io/gh/Informasjonsforvaltning/skolemizer)\n[![PyPI](https://img.shields.io/pypi/v/skolemizer.svg)](https://pypi.org/project/skolemizer/)\n[![Read the Docs](https://readthedocs.org/projects/skolemizer/badge/)](https://skolemizer.readthedocs.io/)\n# skolemizer\nA library with utils for performing Skolemization on blank nodes (RDF)\n\nW3C has a short intro to skolemization here:\nhttps://www.w3.org/2011/rdf-wg/wiki/Skolemisation\n\n## Development\n### Requirements\n- [pyenv](https://github.com/pyenv/pyenv) (recommended)\n- [pipx](https://github.com/pipxproject/pipx) (recommended)\n- [poetry](https://python-poetry.org/)\n- [nox](https://nox.thea.codes/en/stable/)\n- [nox-poetry](https://github.com/cjolowicz/nox-poetry)\n\n```\n% pipx install poetry==1.1.6\n% pipx install nox==2020.12.31\n% pipx inject nox nox-poetry\n```\n### Install\n```\n% git clone https://github.com/Informasjonsforvaltning/skolemizer.git\n% cd skolemizer\n% pyenv install 3.9.4\n% pyenv local 3.9.4\n% poetry install\n```\n### Getting started\nRemember before starting to always set the baseurl for skolemization, according to your organizations url.\nThis can be done by setting the environment variable skolemizer_baseurl on your operation system.\nIt can also e.g be done run time through Python\'s os package:\n```\nos.environ[Skolemizer.baseurl_key] = "https://www.someorganiztion.somedomain/"\n```\nIf not set Skolemizer will use "http://example.com/" as base url.\nIn order to invoke the skolemizer for ensuring identifier of rdf-nodes simply add\n```\nfrom skolemizer import Skolemizer\n```\nand then before rdf-serialization of a class:\n```\n        if not getattr(self, "identifier", None):\n            self.identifier = Skolemizer.add_skolemization()\n```\nThere should also be a skolemization check performed when serializing object properties.\nWhen creating unit tests of skolemized rdf nodes a uuid will be applied as a substring of the complete skolemization.\nTherefore, in order to create stable unit tests one can use the testsutils in order to mock a stable skolemization.\n\nE.g pytest-mock\'s MockFixture permits mocking of the skolemizer:\n```\n    from pytest_mock import MockFixture\n    from skolemizer import skolemization\n\n    catalog = Catalog()\n\n    mocker.patch(\n        "skolemizer.Skolemizer.add_skolemization",\n        return_value=skolemization\n    )\n```\nwhich outputs e.g:\n```\n        @prefix dct: <http://purl.org/dc/terms/> .\n        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n        @prefix dcat: <http://www.w3.org/ns/dcat#> .\n\n        <http://wwww.digdir.no/.well-known/skolem/284db4d2-80c2-11eb-82c3-83e80baa2f94>\n         a dcat:Catalog  .\n\n```\n### Run all sessions\n```\n% nox\n```\n### Run all tests with coverage reporting\n```\n% nox -rs tests\n```\n### Debugging\nYou can enter into [Pdb](https://docs.python.org/3/library/pdb.html) by passing `--pdb` to pytest:\n```\nnox -rs tests -- --pdb\n```\nYou can set breakpoints directly in code by using the function `breakpoint()`.\n',
    'author': 'Stig B. Dørmænen',
    'author_email': 'stigbd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Informasjonsforvaltning/skolemizer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

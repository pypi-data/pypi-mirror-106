# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gallica_autobib', 'gallica_autobib.gallipy']

package_data = \
{'': ['*'], 'gallica_autobib': ['templates/*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'PyPDF4>=1.27.0,<2.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'bibtexparser>=1.2.0,<2.0.0',
 'fuzzysearch>=0.7.3,<0.8.0',
 'fuzzywuzzy>=0.18.0,<0.19.0',
 'jsonpickle>=2.0.0,<3.0.0',
 'lark-parser>=0.11.3,<0.12.0',
 'lxml>=4.6.3,<5.0.0',
 'pydantic>=1.5.1,<2.0.0',
 'python-Levenshtein>=0.12.2,<0.13.0',
 'python-slugify>=5.0.2,<6.0.0',
 'requests-downloader>=0.1.6,<0.2.0',
 'rfc3987>=1.3.8,<2.0.0',
 'rispy>=0.6.0,<0.7.0',
 'roman>=3.3,<4.0',
 'scikit-image>=0.18.1,<0.19.0',
 'sqlitedict>=1.7.0,<2.0.0',
 'sruthi>=0.1.2,<0.2.0',
 'typer>=0.3.2,<0.4.0',
 'xdg>=5.0.2,<6.0.0',
 'xmltodict>=0.12.0,<0.13.0']

entry_points = \
{'console_scripts': ['gallica-autobib = gallica_autobib.cli:app']}

setup_kwargs = {
    'name': 'gallica-autobib',
    'version': '0.1.6',
    'description': 'Automatically match Bibliographies against bnf.gallica.fr',
    'long_description': '# pygallica-autobib\n\n<p align="center">\n    <em>Automatically match Bibliographies against bnf.gallica.fr!</em>\n</p>\n\n<p align="center">\n<a href="https://github.com/2e0byo/pygallica-autobib/actions?query=workflow%3ATest" target="_blank">\n    <img src="https://github.com/2e0byo/pygallica-autobib/workflows/Test/badge.svg" alt="Test">\n</a>\n<a href="https://github.com/2e0byo/pygallica-autobib/actions?query=workflow%3APublish" target="_blank">\n    <img src="https://github.com/2e0byo/pygalln=dependabot" alt="Dependabot Enabled">\n</a>\n<a href="https://codecov.io/gh/2e0byo/pygallica-autobib" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/2e0byo/pygallica-autobib?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/gallica-autobib" target="_blank">\n    <img src="https://img.shields.io/pypi/v/gallica-autobib?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/gallica-autobib/" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/gallica-autobib.svg" alt="Python Versions">\n</a>\n</p>\n\n\n## Standalone Usage\n\n```bash\ngallica-autobib my-bibliography.bib pdfs # match my-bibliography and put files in ./pdfs\ngallica-autobib --help\n```\n\n## As a library\n```python\nfrom pathlib import Path\nfrom gallica_resource.pipeline import BibtexParser\n\nparser = BibtexParser(Path("outdir"))\n\nwith Path("articles.bib").open() as f:\n    parser.read(f)\n\nparser.run()\nfor result in parser.results:\n    print(result)\n```\n\nGallica-Autobib is capable of much more than this. For more information, see the\n[homepage](2e0byo.github.io/pygallica-autobib).\n\n',
    'author': 'John Morris',
    'author_email': '2e0byo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

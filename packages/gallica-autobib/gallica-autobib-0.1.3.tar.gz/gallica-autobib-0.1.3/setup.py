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
 'sruthi>=0.1.2,<0.2.0',
 'typer>=0.3.2,<0.4.0',
 'xmltodict>=0.12.0,<0.13.0']

entry_points = \
{'console_scripts': ['gallica-autobib = gallica_autobib.cli:app']}

setup_kwargs = {
    'name': 'gallica-autobib',
    'version': '0.1.3',
    'description': 'Automatically match Bibliographies against bnf.gallica.fr',
    'long_description': '# pygallica-autobib\n\n<p align="center">\n    <em>Automatically match Bibliographies against bnf.gallica.fr!</em>\n</p>\n\n<p align="center">\n<a href="https://github.com/2e0byo/pygallica-autobib/actions?query=workflow%3ATest" target="_blank">\n    <img src="https://github.com/2e0byo/pygallica-autobib/workflows/Test/badge.svg" alt="Test">\n</a>\n<a href="https://github.com/2e0byo/pygallica-autobib/actions?query=workflow%3APublish" target="_blank">\n    <img src="https://github.com/2e0byo/pygallica-autobib/workflows/Publish/badge.svg" alt="Publish">\n</a>\n<a href="https://dependabot.com/" target="_blank">\n    <img src="https://flat.badgen.net/dependabot/2e0byo/pygallica-autobib?icon=dependabot" alt="Dependabot Enabled">\n</a>\n<a href="https://codecov.io/gh/2e0byo/pygallica-autobib" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/2e0byo/pygallica-autobib?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/gallica-autobib" target="_blank">\n    <img src="https://img.shields.io/pypi/v/gallica-autobib?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/gallica-autobib/" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/gallica-autobib.svg" alt="Python Versions">\n</a>\n</p>\n\n## Overview\n\n`pygallica-autobib` will match your bibliographies against the French National\nLibrary and download articles as pdfs if possible, optionally post-processing\nthem.  Whilst it obviously cannot download articles which Gallica does not hold,\nit strives to achieve a 100% match rate. If you find an article it does not\nmatch, please [report a bug](https://github.com/2e0byo/pygallica-autobib/issues).\n\nFeatures:\n\n- Input in RIS or Bibtex format\n- Output report generated with a jinja template (templates for org-mode, html\n  and plaintext supplied)\n\n\n## Online Demo\n\nThere is an [online demo](https://phd.2e0byo.co.uk/gallica) with a very basic\ninterface, allowing\n\n## Installation\n\nYou need python >= 3.9 (but if anyone needs to use this with an older python,\nopen an issue and I will refactor the few incompatible statements).  Then\ninstall as usual:\n\n```bash\npipx install gallica-autobib # prefered, if you have pipx, or\npython -m pip install gallica-autobib\n```\n\n## Standalone Usage\n\n```bash\ngallica-autobib my-bibliography.bib pdfs # match my-bibliography and put files in ./pdfs\ngallica-autobib --help\n```\n\n## As a library\n```python\n\nfrom pathlib import Path\nfrom gallica_autobib.models import Article\nfrom gallica_autobib.query import Query, GallicaResource\n\ntarget = Article(\n    journaltitle="La Vie spirituelle",\n    author="M.-D. Chenu",\n    pages=list(range(547, 552)),\n    volume=7,\n    year=1923,\n    title="Ascèse et péché originel",\n)\nquery = Query(target)\ncandidate = Query.run().candidate # get candidate journal\ngallica_resource = GallicaResource(candidate, source)\nark = gallica_resource.ark # match candidate article\ngallica_resource.download_pdf(Path("article.pdf"))\n```\n\nor if you just want to do what the cli does:\n\n```python\nfrom pathlib import Path\nfrom gallica_resource.pipeline import BibtexParser\n\nparser = BibtexParser(Path("outdir"))\n\nwith Path("articles.bib").open() as f:\n    parser.read(f)\n\nparser.run()\nfor result in parser.results:\n    print(result)\n```\n\nfor more advanced usage see the documentation and the test suite.\n\n\n## Developing\n\n```bash\n\n# ensure you have Poetry installed\npip install --user poetry\n\n# install all dependencies (including dev)\npoetry install\n```\n\nWhen your feature is ready, open a PR.\n\n## Testing\nWe use pytest and mypy.  You may want to focus on getting unit tests passing\nfirst:\n\n```bash\npoetry run pytest --cov=gallica_autobib --cov-report html --cov-branch tests\n```\n\nIf you have started a shell with `poetry shell` you can drop the `poetry run`.\n\nWhen unittests are passing you can run the whole suite with:\n\n```bash\npoetry run scripts/test.sh\n```\n\nNote that tests will only pass fully if `/tmp/` exists and is writeable, and if\n`poppler` and `imagemagick` are installed.  This is due to the use of\n`pdf-diff-visually` and the rather hackish template tests.\n \nYou may wish to check your formatting first with\n\n```bash\npoetry run scripts/format.sh\n```\n\nAlternatively, just open a premature PR to run the tests in CI.  Note that this\nis rather slow.\n\n## Plausibly Askable Questions\n\n### Why don\'t you also check xyz.com?\nBecause I don\'t know about it.  Open an issue and I\'ll look into it.\n\n### Why don\'t you use library xyz for image processing?\nProbably because I don\'t know about it.  This is a quick tool written to help me\nresearch.  Submit a PR and I\'ll happily update it.\n\n### Why is the code so verbose?\nIt is rather object-oriented.  It might be rather over engineered. It was\nwritten in a hurry and the design evolved as it went along.  On the other hand,\nit should be easier to extend.\n\n### Why not just extend pygallica?\nI mean to submit the SRU stuff as an extension to `pygallica`\n\n',
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

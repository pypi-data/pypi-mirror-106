# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spacypdfreader']

package_data = \
{'': ['*']}

install_requires = \
['pdfminer.six>=20201018,<20201019',
 'rich>=10.2.2,<11.0.0',
 'spacy>=3.0.6,<4.0.0']

setup_kwargs = {
    'name': 'spacypdfreader',
    'version': '0.1.0',
    'description': 'A PDF to text extraction pipeline component for spaCy.',
    'long_description': '# spaCyPDFreader\n\nExtract text from pdfs using spaCy and capture the page number as a spacy extension.\n\n## Installation\n\n```bash\npip install spacypdfreader\n```\n\n## Usage\n\n\n```python\nimport spacy\nfrom spacypdfreader import pdf_reader\n\nnlp = spacy.load("en_core_web_sm")\ndoc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace">Extracting text from <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span> pdf pages<span style="color: #808000; text-decoration-color: #808000">...</span>\n</pre>\n\n\n\n    100%|██████████| 4/4 [00:00<00:00,  5.97it/s]\n\n\n\n```python\ndoc[0:10]\n```\n\n\n\n\n    Test PDF 01\n    \n    This is a simple test pdf\n\n\n\n\n```python\nfor token in doc[0:10]:\n    print(f"Token: `{token}`, page number  {token._.page_number}")\n```\n\n    Token: `Test`, page number  1\n    Token: `PDF`, page number  1\n    Token: `01`, page number  1\n    Token: `\n    \n    `, page number  1\n    Token: `This`, page number  1\n    Token: `is`, page number  1\n    Token: `a`, page number  1\n    Token: `simple`, page number  1\n    Token: `test`, page number  1\n    Token: `pdf`, page number  1\n\n\n\n```python\ndoc[-10:]\n```\n\n\n\n\n    U3D or PRC and various other data formats.[15][16][17]\n    \n\n\n\n\n\n```python\nfor token in doc[-10:]:\n    print(f"Token: `{token}`, page number  {token._.page_number}")\n```\n\n    Token: `U3D`, page number  4\n    Token: `or`, page number  4\n    Token: `PRC`, page number  4\n    Token: `and`, page number  4\n    Token: `various`, page number  4\n    Token: `other`, page number  4\n    Token: `data`, page number  4\n    Token: `formats.[15][16][17`, page number  4\n    Token: `]`, page number  4\n    Token: `\n    \n    \x0c`, page number  4\n\n',
    'author': 'SamEdwardes',
    'author_email': 'edwardes.s@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SamEdwardes/spaCyPDFreader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

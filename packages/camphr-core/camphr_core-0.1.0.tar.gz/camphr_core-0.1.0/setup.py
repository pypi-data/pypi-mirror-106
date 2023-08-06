# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_core',
 'camphr_core.lang',
 'camphr_core.lang.juman',
 'camphr_core.lang.mecab',
 'camphr_core.lang.sentencepiece',
 'camphr_core.ner_labels']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'more-itertools>=8.7.0,<9.0.0',
 'spacy>=2.2,<=2.3.5',
 'typing-extensions>=3.7.4']

extras_require = \
{'all': ['fugashi>=1.1.0,<2.0.0',
         'ipadic>=1.0.0,<2.0.0',
         'mecab-python3>=1.0.3,<2.0.0',
         'sentencepiece>=0.1.95,<0.2.0',
         'sentencepiece>=0.1.95,<0.2.0',
         'pyknp>=0.4.2,<0.5.0',
         'mojimoji>=0.0.11,<0.0.12'],
 'juman': ['pyknp>=0.4.2,<0.5.0', 'mojimoji>=0.0.11,<0.0.12'],
 'mecab': ['fugashi>=1.1.0,<2.0.0',
           'ipadic>=1.0.0,<2.0.0',
           'mecab-python3>=1.0.3,<2.0.0'],
 'sentencepiece': ['sentencepiece>=0.1.95,<0.2.0']}

entry_points = \
{'spacy_languages': ['ja_juman = camphr_core.lang.juman:Japanese',
                     'ja_mecab = camphr_core.lang.mecab:Japanese',
                     'sentencepiece = '
                     'camphr_core.lang.sentencepiece:SentencePieceLang']}

setup_kwargs = {
    'name': 'camphr-core',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'tamuhey',
    'author_email': 'tamuhey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PKSHATechnology-Research/camphr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

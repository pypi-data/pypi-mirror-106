# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_transformers']

package_data = \
{'': ['*']}

install_requires = \
['camphr_torch>=0.1.0,<0.2.0',
 'dataclass-utils>=0.7.10,<0.8.0',
 'pytokenizations>=0.8.3,<0.9.0',
 'transformers>=3.0,<3.1',
 'typing-extensions>=3.7.4']

entry_points = \
{'spacy_factories': ['transformers_model = '
                     'camphr_transformers:TrfModel.from_nlp',
                     'transformers_ner = '
                     'camphr_transformers:TrfForNamedEntityRecognition.from_nlp',
                     'transformers_sequece_classifier = '
                     'camphr_transformers:TrfForSequenceClassification.from_nlp',
                     'transformers_sequence_classifier = '
                     'camphr_transformers:TrfForSequenceClassification.from_nlp',
                     'transformers_tokenizer = '
                     'camphr_transformers:TrfTokenizer.from_nlp']}

setup_kwargs = {
    'name': 'camphr-transformers',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Yohei Tamura',
    'author_email': 'tamuhey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

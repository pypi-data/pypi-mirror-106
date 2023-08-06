# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emailable']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'emailable-backport',
    'version': '1.0.0',
    'description': 'This is the backport to python 2.7 of the official python wrapper for the Emailable API.',
    'long_description': "# Emailable Python Library Backport\n\n![License](https://img.shields.io/pypi/l/emailable-backport)\n![Python versions](https://img.shields.io/pypi/pyversions/emailable-backport)\n![Version](https://img.shields.io/pypi/v/emailable-backport)\n\nThis is the backport to Python 2.7 of the [Emailable's](https://github.com/emailable) official [python wrapper](https://github.com/emailable/emailable-python) for the Emailable API.\n\n## Documentation\n\nSee the [Python API docs](https://emailable.com/docs/api/?python).\n\n## Installation\n\n```shell\npip install emailable-backport\n```\n\n## Usage\n\nThe library needs to be configured with your account's API key which is available in your [Emailable Dashboard](https://app.emailable.com/api).\n\n### Setup\n\n```python\nimport emailable\n\nclient = emailable.Client('live_...')\n```\n\n### Verification\n\n```python\n# verify an email address\nresponse = client.verify('evan@emailable.com')\nresponse.state\n=> 'deliverable'\n\n# additional parameters are available. see API docs for additional info.\nclient.verify('evan@emailable.com', smtp=False, accept_all=True, timeout=25)\n```\n\n#### Slow Email Server Handling\n\nSome email servers are slow to respond. As a result, the timeout may be reached\nbefore we are able to complete the verification process. If this happens, the\nverification will continue in the background on our servers. We recommend\nsleeping for at least one second and trying your request again. Re-requesting\nthe same verification with the same options will not impact your credit\nallocation within a 5 minute window.\n\nA slow response will return with a 249 status code.\n\n```python\nresponse = client.verify('slow@example.com')\nresponse.status_code\n=> 249\nresponse.message\n=> 'Your request is taking longer than normal. Please send your request again.'\n```\n\n### Batch Verification\n\n#### Start a batch\n\n```python\nemails = ['evan@emailable.com', 'support@emailable.com', ...]\nresponse = client.batch(emails)\nresponse.id\n=> '5cff27400000000000000000'\n\n# you can optionally pass in a callback url that we'll POST to when the\n# batch is complete.\nresponse = client.batch(emails, callback_url='https://emailable.com/')\n```\n\n#### Get the status / results of a batch\n\nTo get the status of a batch call `batch_status` with the batch's id. If your batch is still being processed, you will receive a message along with the current progress of the batch. When a batch is completed, you can access the results in the `emails` attribute.\n\n```python\nresponse = client.batch_status('5cff27400000000000000000')\n\n# if your batch is still running\nresponse.processed\n=> 1\nresponse.total\n=> 2\nresponse.message\n=> 'Your batch is being processed.'\n\n# if your batch is complete\nresponse.emails\n=> [{'email': 'evan@emailable.com', 'state': 'deliverable'...}, {'email': 'support@emailable.com', 'state': 'deliverable'...}...]\n\n# get the counts\nresponse.total_counts\n=>{'deliverable': 2, 'undeliverable': 0 ...}\nresponse.reason_counts\n=>{'accepted_email': 2, 'rejected_email': 0 ...}\n```\n\n## Development\n\nTests can be run with the following command:\n\n```shell\npoetry run tox\n```\n\n## Contributing\n\nBug reports and pull requests are welcome on GitHub at https://github.com/bernardoduarte/emailable-python-backport.\n",
    'author': 'Bernardo Duarte',
    'author_email': 'bernardoeiraduarte@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bernardoduarte',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)

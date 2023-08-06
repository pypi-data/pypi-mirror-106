# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['worstcase']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.2,<4.0.0', 'scipy>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'worstcase',
    'version': '0.1.0',
    'description': 'Worst case analysis and sensitivity studies using Extreme Value and/or Monte Carlo methods.',
    'long_description': '# worstcase\n\n`pip install worstcase`\n\nWorst case analysis and sensitivity studies using Extreme Value and/or Monte Carlo methods.\n\nEDN blogger Charles Hymowitz wrote an insightful series on worst case circuit analysis, read it [here](https://www.edn.com/the-worst-case/).\n\nThis lightweight package allows the user to specify varying parameters and execute worst case analysis or sensitivity studies by Extreme Value and/or Monte Carlo methods over arbitrary single valued functions. Parameters are assumed to be uniform by default; the user may generate their own custom distributions if desired.\n\nPlease see the [example](./examples/voltage_divider.ipynb) for usage.',
    'author': 'amosborne',
    'author_email': 'amosborne@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/amosborne/worstcase',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)

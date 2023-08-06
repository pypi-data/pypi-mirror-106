# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tw_complex']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.3,<2.0.0', 'scikit-learn>=0.24.2,<0.25.0', 'scipy>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'tw-complex',
    'version': '0.1.0',
    'description': 'Algorithms for TW',
    'long_description': '# TW Complex\n\nRepo with algorithms to divide ally villages into front and back in TW.\n\nUnderneath it is a problem of dividing a set of 2D points **A** according to the `min_radius` and `max_radius` distances from a set of other 2D points **B**, which can be solved most simply by counting the distances from each point in the first set **A** to all points in the second set **B** one by one.\n\n# Examples (before -> after)\n\n### Example 1\n\n```bash\nAlly: 10000 points\nEnemy: 15000 points\nmin_radius: 1.4\nmax_radius: 2\n```\n\n![example1](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_1.png)\n\n### Example 2\n\n```bash\nAlly: 2500 points\nEnemy: 6000 points\nmin_radius: 4\nmax_radius: 10\n```\n\n![example2](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_2.png)\n\n### Example 3\n\n```bash\nAlly: 20000 points\nEnemy: 20000 points\nmin_radius: 20\nmax_radius: 60\n```\n\n![example3](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_3.png)\n\n### Example 4\n\n```bash\nAlly: 20000 points\nEnemy: 20000 points\nmin_radius: 10\nmax_radius: 120\n```\n\n![example4](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_4.png)\n',
    'author': 'rafsaf',
    'author_email': 'rafal.safin12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rafsaf/tw-complex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)

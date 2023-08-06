# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['understory',
 'understory.mkdn',
 'understory.mkdn.block',
 'understory.mkdn.inline',
 'understory.mm',
 'understory.uri',
 'understory.web',
 'understory.web.framework',
 'understory.web.framework.templates',
 'understory.web.headers',
 'understory.web.indie',
 'understory.web.indie.indieauth',
 'understory.web.indie.indieauth.templates',
 'understory.web.indie.micropub',
 'understory.web.indie.micropub.templates',
 'understory.web.indie.microsub',
 'understory.web.indie.microsub.templates',
 'understory.web.indie.templates',
 'understory.web.indie.webmention',
 'understory.web.indie.websub',
 'understory.web.response']

package_data = \
{'': ['*'],
 'understory.web.framework': ['static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css'],
 'understory.web.indie.webmention': ['templates/*'],
 'understory.web.indie.websub': ['templates/*']}

install_requires = \
['gunicorn>=20.1.0,<21.0.0',
 'hstspreload>=2020.12.22,<2021.0.0',
 'lxml>=4.6.3,<5.0.0',
 'mf2py>=1.1.2,<2.0.0',
 'mf2util>=0.5.1,<0.6.0',
 'pendulum>=2.1.2,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'understory-code>=0.0.1,<0.0.2',
 'understory-db>=0.0.1,<0.0.2',
 'understory-fx>=0.0.1,<0.0.2',
 'understory-term>=0.0.1,<0.0.2']

entry_points = \
{'console_scripts': ['web = understory.web.__main__:main'],
 'web.apps': ['indieauth-client = understory.web.indie.indieauth:client',
              'indieauth-server = understory.web.indie.indieauth:server',
              'micropub = understory.web.indie.micropub:server',
              'microsub = understory.web.indie.microsub:server',
              'webmention = understory.web.indie.webmention:receiver',
              'websub = understory.web.indie.websub:hub']}

setup_kwargs = {
    'name': 'understory-web',
    'version': '0.0.4',
    'description': 'Tools for metamodern web development',
    'long_description': '# understory-web\nTools for metamodern web development\n',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@lahacker.net',
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

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gqlalchemy']

package_data = \
{'': ['*']}

install_requires = \
['pymgclient>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'gqlalchemy',
    'version': '1.0.2',
    'description': 'GQLAlchemy is library developed with purpose of assisting writing and running queries on Memgraph.',
    'long_description': 'GQLAlchemy\n=================\n\n<p align="left">\n    <a href="https://github.com/memgraph/gqlalchemy/actions" alt="Actions"> <img src="https://img.shields.io/github/workflow/status/memgraph/gqlalchemy/Build%20and%20Test" /></a>\n</p>\n\nGQLAlchemy is library developed with purpose of assisting writing and running\nqueries on Memgraph. GQLAlchemy supports high-level connection to Memgraph\nas well as modular query builder.\n\nGQLAlchemy is built on top of Memgraph\'s low-level client pymgclient\n([pypi](https://pypi.org/project/pymgclient/) /\n[documentation](https://memgraph.github.io/pymgclient/) /\n[GitHub](https://github.com/memgraph/pymgclient)).\n\nInstallation\n------------\nTo install `gqlalchemy`, simply run the following command:\n```\npip install gqlalchemy\n```\n\nMatch Example\n--------------\n\nWhen working with the `pymgclient`, Python developer can connect to database\nand execute `MATCH` cypher query with following syntax:\n\n```python\nimport mgclient\n\nconn = mgclient.connect(host=\'127.0.0.1\', port=7687)\n\ncursor = conn.cursor()\ncursor.execute("""\n    MATCH (from:Node)-[:Connection]->(to:Node)\n    RETURN from, to;\n""")\nresult = cursor.fetchone()\nconn.commit()\n\nfor result in results:\n    print(result[\'from\'])\n    print(result[\'to\'])\n```\n\nAs we can see, example above can be error-prone, because we do not have\nabstractions for creating a database connection and `MATCH` query.\n\nNow, rewrite the exact same query by using the functionality of `gqlalchemy`.\n\n```python\n\nfrom gqlalchemy import Match, Memgraph\n\nmemgraph = Memgraph()\n\nresults = Match().node("Node",variable="from")\n                 .to("Connection")\n                 .node("Node",variable="to")\n                 .execute()\n\nfor result in results:\n    print(result[\'from\'])\n    print(result[\'to\'])\n```\n\nLicense\n-------\n\nCopyright (c) 2016-2021 [Memgraph Ltd.](https://memgraph.com)\n\nLicensed under the Apache License, Version 2.0 (the "License"); you may not use\nthis file except in compliance with the License. You may obtain a copy of the\nLicense at\n\n     http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software distributed\nunder the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\nCONDITIONS OF ANY KIND, either express or implied. See the License for the\nspecific language governing permissions and limitations under the License.\n',
    'author': 'Jure Bajic',
    'author_email': 'jure.bajic@memgraph.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/memgraph/gqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

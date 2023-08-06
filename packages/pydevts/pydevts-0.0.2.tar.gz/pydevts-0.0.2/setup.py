# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydevts']

package_data = \
{'': ['*']}

install_requires = \
['trio>=0.18.0,<0.19.0']

setup_kwargs = {
    'name': 'pydevts',
    'version': '0.0.2',
    'description': 'pydevts (PYthon Distributed Data Store) Is a distributed data store and message service based ont he concept of nodes and built with python.',
    'long_description': "# pydevts\n\npydevts (Python Distributed Data System) is a distributed event system written in python and based on the concept of nodes that is designed for the implementation of data stores and other replicated systems.\n\npydevts is based upon a simple concept: A cluster of nodes that can send and recieve events.\n\npydevts is also lightweight, requiring only the external library [trio](https://github.com/python-trio/trio) although some examples may require additional libraries (these will be detailed in the examples description)\n\n\n## How do I use this?\n\nWhile more in-depth documentation will come in the future, currently there are several examples in the `examples/` folder.\n\nEach example takes some command line arguments, which are detailed below. But first, we must define a few terms.\n\n### Terms\n\n\n#### Cluster Ports\n\nA cluster port is a port with which a client will try to connect to a cluster. If the port is not reachable, the node starts as the first node in a cluster. A cluster port is any public port of a node in a cluster. Cluster ports are printed when a node starts and log level is INFO or DEBUG.\n\n#### Host Ports\n\nSometimes pydevts Nodes will run another application alongside themselves when running. If this application is a server of some kind, it's public facing port is called a Host Port.\n\n### Examples\n\nListed below are some of the examples found in the `examples/` directory. All examples assume localhost.\n\n#### fastapi_example.py\n\nExternal Requirements:\n- fastapi\n- hypercorn\n\nThis example details how to run another async application (FastAPI with hypercorn) alongside pydevts.\n\nIt takes two arguments:\n- The cluster port to attempt to connect to\n- The host port to host the fastapi application on\n\n#### picklenode.py\n\nExternal Requirements:\n- None\n\nNOTICE: This should never be used with untrusted data, as pickle can be used to execute untrusted code.\n\nThis example shows how to create a custom node type. This node stores a single pickled object, and can get and set the object in the cluster.\n\nThis example takes two arguments:\n- The cluster port to attempt to connect to\n- The literal string 'w' (without the quotes) if we want the cluster to update the value. If we do not provide this, the cluster will simply read the value every second and print it.\n\n#### picklenodewriter.py\n\nExternal Requirements:\n- None\n\nNOTICE: This should never be used with untrusted data, as pickle can be used to execute untrusted code.\n\nThis example works in conjunction with picklenode.py to show two different nodes types can work together. Every time the stored value in a picklenode.py node is updated, it writes the string representation of it to a file called `pickleoutput.txt`\n\nThis example takes one argument:\n- The cluster port to attempt to connect to\n\n## Collaboration and Questions\n\nIf you find a bug, report it on github issues. If, however, you have questions or are not sure how something works, post it on github discussions.\n\nIf you see some room for improvement and you wish to help out, create a github issue describing the problem and stating that you can work on it. If you do not wish to help out, or can not for some reason, then still leave the issue, as any feedback is appreciated. Usability and efficiency feedback is appreciated even more.",
    'author': 'Riley Wilton',
    'author_email': 'meetingprince34@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Peperworx/pydevts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

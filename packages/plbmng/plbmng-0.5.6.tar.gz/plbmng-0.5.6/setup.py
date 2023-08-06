# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plbmng', 'plbmng.lib', 'plbmng.utils']

package_data = \
{'': ['*'], 'plbmng': ['database/*']}

install_requires = \
['dynaconf>=3.1.4,<4.0.0',
 'folium>=0.12.1,<0.13.0',
 'geocoder>=1.38.1,<2.0.0',
 'gevent>=21.1.2,<22.0.0',
 'loguru>=0.5.3,<0.6.0',
 'parallel-ssh>=2.5.4,<3.0.0',
 'paramiko>=2.7.2,<3.0.0',
 'pysftp>=0.2.9,<0.3.0',
 'pythondialog>=3.5.1,<4.0.0',
 'vincent>=0.4.4,<0.5.0']

entry_points = \
{'console_scripts': ['plbmng = plbmng.__main__:main']}

setup_kwargs = {
    'name': 'plbmng',
    'version': '0.5.6',
    'description': 'Tool for monitoring PlanetLab network',
    'long_description': "======\nplbmng\n======\n\n.. image:: source/images/plbmng.png\n    :scale: 50 %\n    :alt: plbmng main menu\n    :align: center\n\nDescription\n-----------\n``plbmng`` is a tool for monitoring servers within and outside of Planetlab network.\n\nFor this purpose there are several tools within this project:\n        - to get all servers from PlanetLab network and gather all available information about them\n        - to create a map with pin pointed location of the servers\n        - filter servers based on their availability, location, software, hardware.\n        - to add server which are not from PlanetLab network into plbmng database\n        - copy file/files to multiple server/servers from plbmng database\n\n\nDependencies\n------------\n        - Python 3.5 or higher\n        - Dialog engine(TUI)\n        - Python modules (all modules are available from pip):\n                - geocoder\n                - folium\n                - numpy\n                - vincent\n                - pandas\n                - paramiko\n                - pythondialog\n\nInstallation\n------------\nTo install the plbmng module, type:\n\n.. code-block:: bash\n\n         $ pip3 install plbmng\n\nInstall dialog-like engine. If you are using Fedora-like distributions:\n\n.. code-block:: bash\n\n        $ sudo yum install -y dialog\n\nBasic usage\n-----------\nWhen you run plbmng for the first time, please add your credentials for Planetlab network. If you don't want to add your credentials right away, you can skip it and add it in the settings later.\n\nOnce you have added your credentials, use ``Update server list now`` option in the Monitor servers menu. In default you will have old data which can be updated by this function. It downloads all servers from your slice and exports it as ``default.node`` file.\n\n``Main menu``\n\n``Access servers``: If you are looking for some specific node or set of nodes, use ``Access servers`` option. In the next screen you can choose from four options: access last server, search by DNS, IP or location. If you choose search by DNS or IP you will be prompted to type a string, which indicates the domain you are looking for. If you want to search by location, you will be asked to choose a continent and a country. Then you will see all available nodes from this selected country and you can choose one of them to see more detailes about this particular node. At the bottom of the information screen you can choose from three options.\n\n``Monitor servers``: Monitoring tools are there.\n                 -  ``Update server list now``, here you can update your list of servers.\n                 -  ``Update server status now``, here you can update your list of available servers.\n\n``Plot servers on map``:\n             ``Generate map``, will create a map with all or specific nodes from ``planetlab.node`` file.\n``Set credentials``:\n      Will open interactive editor for you to insert your credentials to PlanetLab network.\n\nExtras\n------\nIn the extras menu you can find tool for managing your own server by adding them to the database. Another new feature added to extras menu is parallel copy to server/servers from database.\n\n``Add server to database``: Allows user to add a server to the plbmng database. By adding info about server to the prepared file, you are able to filter and monitor your server with this tool just like with the others within PlanetLab network.\n\n``Copy files to server/servers``: User is prompted to select file/files, server/servers from plbmng database and destination path on the target. DO NOT FORGET TO SET PATH TO SSH KEY AND SLICE NAME(user on the target) IN THE CONFIG FILE!\n\n\n\nAuthors\n-------\n\n- `Dan Komosny`_ - Maintainer and supervisor\n- `Ivan Andrasov`_ - Contributor\n- `Filip Suba`_ - Contributor\n- `Martin Kacmarcik`_ - Contributor\n\n\n.. _`Ivan Andrasov`: https://github.com/Andrasov\n.. _`Filip Suba`: https://github.com/fsuba\n.. _`Dan Komosny`: https://www.vutbr.cz/en/people/dan-komosny-3065\n.. _`Martin Kacmarcik`: https://github.com/xxMAKMAKxx\n",
    'author': 'Ivan Andrasov',
    'author_email': 'andrassk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/utko-planetlab/plbmng/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

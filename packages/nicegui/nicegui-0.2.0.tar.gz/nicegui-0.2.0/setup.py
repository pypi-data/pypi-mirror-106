# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nicegui', 'nicegui.elements']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.9.0,<3.0.0',
 'binding>=0.1.1,<0.2.0',
 'docutils>=0.17.1,<0.18.0',
 'justpy==0.1.5',
 'markdown2>=2.4.0,<3.0.0',
 'matplotlib>=3.4.1,<4.0.0',
 'typing-extensions>=3.10.0,<4.0.0']

setup_kwargs = {
    'name': 'nicegui',
    'version': '0.2.0',
    'description': 'High-Level Abstraction Web-GUI Using Just Python',
    'long_description': '# NiceGUI\n\n<img src="https://raw.githubusercontent.com/zauberzeug/nicegui/main/sceenshots/ui-elements.png" width="300" align="right">\n\nWe like [Streamlit](https://streamlit.io/) but find it does to much magic when it comes to state handling. In search for an alernative nice library to write simple graphical user interfaces in Python we discovered [justpy](https://justpy.io/). While too "low-level-html" for our daily usage it provides a great basis for "NiceGUI".\n\n## Purpose\n\nNiceGUI is intended to be used for small scripts and user interfaces with a very limited user base. Custom "Smart-Home Control" solutions or "Robotics" for example. It\'s also helpful for development like tweaking/configuring a machine learning training or tuning motor controllers.\n\n## Features\n\n- browser-based GUI\n- shared state between multiple browser windows\n- implicit reload on code change\n- clean set of GUI elements (label, button, checkbox, switch, slider, input, ...)\n- simple grouping with rows, columns and cards\n- genral-purpose html and markdown elements\n- built-in timer to refresh data in intervals (even every 10 ms)\n- straight-forward data bindings to write even less code\n\n## Install\n\n```bash\npython3 -m pip install nicegui\n```\n\n## Usage\n\nWrite your nice GUI in a file `main.py`:\n\n```python\nfrom nicegui import ui\n\nui.label(\'Hello NiceGUI!\')\nui.button(\'BUTTON\', on_click=lambda: print(\'button was pressed\'))\n```\n\nLaunch it with:\n\n```bash\npython3 main.py\n```\n\nNote: The script will automatically reload the GUI if you modify your code.\n\n## API\n\nAPI Reference is hosted at [https://nicegui.io](https://nicegui.io). Also have a look at [examples.py](https://github.com/zauberzeug/nicegui/tree/main/examples.py) for an extensive demonstration what you can do with NiceGUI.\n',
    'author': 'Zauberzeug GmbH',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zauberzeug/nicegui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

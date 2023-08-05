# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nicegui', 'nicegui.elements']

package_data = \
{'': ['*']}

install_requires = \
['justpy==0.1.5',
 'matplotlib>=3.4.1,<4.0.0',
 'typing-extensions>=3.10.0,<4.0.0']

setup_kwargs = {
    'name': 'nicegui',
    'version': '0.1.6',
    'description': 'High-Level Abstraction Web-GUI Using Just Python',
    'long_description': '# NiceGUI\n\n<img src="sceenshots/ui-elements.png?raw=true" width="300" align="right">\n\nWe like [Streamlit](https://streamlit.io/) but find it does to much magic when it comes to state handling. In search for an alernative nice library to write simple graphical user interfaces in Python we discovered [justpy](https://justpy.io/). While too "low-level-html" for our daily usage it provides a great basis for our shot at a "NiceGUI".\n\n## Features\n\n- browser-based GUI\n- implicit reload on code change\n- clean set of GUI elements (label, button, checkbox, switch, slider, input, ...)\n- simple grouping with rows, columns and cards\n- built-in timer to refresh data in intervals (even every 10 ms)\n\n## Usage\n\nWrite your nice GUI in a file `main.py`:\n\n```python\nfrom nicegui import ui\n\nui.label(\'Hello NiceGUI!\')\nui.button(\'BUTTON\', on_click=lambda: print(\'button was pressed\'))\n```\n\nLaunch it with:\n\n```bash\npython3 main.py\n```\n\nNote: The script will automatically reload the GUI if you modify your code.\n\n## API\n\nSee [main.py](/main.py) for an example of all API calls you can make with NiceGUI.\n\n## Plots\n\n<img src="sceenshots/live-plot.gif?raw=true" width="400" align="right">\n\n```python\nlines = ui.line_plot(n=2, limit=20).with_legend([\'sin\', \'cos\'], loc=\'upper center\', ncol=2)\nui.timer(0.1, lambda: lines.push([datetime.now()], [\n    [np.sin(datetime.now().timestamp()) + 0.02 * np.random.randn()],\n    [np.cos(datetime.now().timestamp()) + 0.02 * np.random.randn()],\n]))\n```\n',
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

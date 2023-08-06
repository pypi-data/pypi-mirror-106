# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prey', 'prey.bin']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-requests>=0.1.3,<0.2.0',
 'aiohttp>=3.7.4,<4.0.0',
 'colorama>=0.4.4,<0.5.0']

entry_points = \
{'console_scripts': ['prey = prey.bin:main']}

setup_kwargs = {
    'name': 'prey',
    'version': '0.1.3',
    'description': 'A tool for writing shell scripts in python.',
    'long_description': '# prey\n```py\n#!/usr/bin/env prey\n\nasync def main():\n    await x("cat pyproject.toml | grep name")\n\n    branch = await x("git branch --show-current")\n    await x(f"dep deploy --branch={branch}")\n\n    await x(\n        [\n            "sleep 1; echo 1",\n            "sleep 2; echo 2",\n            "sleep 3; echo 3",\n        ]\n    )\n\n    name = "foo bar"\n    await x(f"mkdir /tmp/${name}")\n```\n\nA tool for writing shell scripts in Python. Inspired by [google/zx](https://github.com/google/zx). This package provides a wrapper around `asyncio.subprocess`. If you\'re looking for a more complete solution you may want to check out [zxpy](https://github.com/tusharsadhwani/zxpy).\n\n\n## Install\n```bash\npip install prey\n```\n\n## Documentation\nWrap your scripts in an async function called **`main`**:\n```py\nasync def main():\n    # script...\n```\nIt must be called `main` as the executable looks for a function calls main and calls it. This is used so commands can be asynchronous.\n\nYou can add the shebang at the top of your script:\n```py\n#!/usr/bin/env prey\n```\nand run it like so:\n```bash\nchmod +x ./script.py\n./script.py\n```\n\nOr via the `prey` executable:\n```bash\nprey ./script.py\n```\nWhen using `prey` via the executable or a shebang, all of the functions (`x`, `colorama`, `request`, etc) are available wihtout any imports.\n\n### `await x("command")`\nAsychronously executes a given string using the `create_subprocess_shell` function from the `asyncio.subprocess` module and returns the output.\n```py\ncount = int(await x("ls -1 | wc -l"))\nprint(f"Files count: {count}")\n```\n\n### `cd("filepath")`\nChanges the current working directory.\n```py\ncd("/tmp")\nawait x(\'pwd\') # outputs /tmp\n```\n\n### colorama package\nThe [colorama]() package is available without importing inside scripts.\n```py\nprint(f"{colorama.Fore.BLUE}Hello World!")\n```\n\n### request package\nA wrapper around aiohttp, [aiohttp-requests](https://pypi.org/project/aiohttp-requests/)`.requests.session.request`, is available without importing inside scripts.\n```py\nresponse = await request("get", "http://python.org")\nhtml = await response.text()\n```\n\n### Importing from other scripts\nIt is possible to make use of `x` and other functions via explicit imports:\n```py\n#!/usr/bin/env prey\nfrom prey import x\nawait x(\'date\')\n```\n\n### Passing env variables\n```py\nos.environ["FOO"] = "bar"\nawait x(\'echo $FOO\')\n```',
    'author': 'Sachin Raja',
    'author_email': 'sachinraja2349@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cloudagon/prey',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)

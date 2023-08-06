# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pupalink']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0', 'beautifulsoup4>=4.9.3,<5.0.0', 'lxml>=4.6.3,<5.0.0']

setup_kwargs = {
    'name': 'pupalink',
    'version': '0.1.0a2',
    'description': 'Springer Link Download Module for Python',
    'long_description': '# pupalink\nby [aykxt](https://github.com/aykxt) and [billaids](https://github.com/billaids/)\n\n## Only for educational purposes!\n---\n## Features\n- Search and download books from Springer Link\n\n## How to start?\n- You need an active Springer Link access\n- Use from your cookie the value from parameter "idp_session"\n\n<div class="termy">\n\n```console\n$ from pupalink import Session\n\n$ session = Session("YOUR_IDP_SESSION)\n\n```\n</div>\n\n## Example \n\n<div class="termy">\n\n```python\nfrom pupalink import Session\nfrom asyncio import get_event_loop\n\nasync def main():\n    session = Session("YOUR_KEY")\n    books = await session.search_book("Rust")\n\n    for book in books:\n        await session.download_book(book)\n\n    await session.close()\n\n\nloop = get_event_loop()\nloop.run_until_complete(main())\n\n```\n</div>',
    'author': 'Jimmy Nelle',
    'author_email': 'jimmy.nelle@hsw-stud.de',
    'maintainer': 'Jimmy Nelle',
    'maintainer_email': 'jimmy.nelle@hsw-stud.de',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

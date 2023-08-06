# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['session_keeper', 'session_keeper.keeper', 'session_keeper.storage']

package_data = \
{'': ['*']}

install_requires = \
['Telethon>=1.21.1,<2.0.0',
 'cryptography>=3.4.7,<4.0.0',
 'tabulate>=0.8.9,<0.9.0']

entry_points = \
{'console_scripts': ['session-keeper = session_keeper:CLIKeeper.run']}

setup_kwargs = {
    'name': 'tg-session-keeper',
    'version': '0.1.2',
    'description': 'Консольная утилита для хранения Telegram-сессий.',
    'long_description': '# Telegram Session Keeper\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tg-session-keeper?logo=python&style=flat-square)](https://python.org)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/tg-session-keeper?style=flat-square)](https://pypi.org/project/tg-session-keeper)\n[![PyPi Package Version](https://img.shields.io/pypi/v/tg-session-keeper?style=flat-square)](https://pypi.org/project/tg-session-keeper)\n[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/DavisDmitry/tg-session-keeper/Tests/master?label=tests&style=flat-square)](https://github.com/DavisDmitry/tg-session-keeper/actions/workflows/tests.yml)\n[![GitHub](https://img.shields.io/github/license/DavisDmitry/tg-session-keeper?style=flat-square)](https://github.com/DavisDmitry/tg-session-keeper/raw/master/LICENSE)\n[![Telethon](https://img.shields.io/badge/Telethon-blue?style=flat-square)](https://github.com/LonamiWebs/Telethon)\n\nКонсольная утилита для хранения Telegram-сессий.\n\nЯ использую несколько аккаунтов Telegram. Большинство из них зарегистрированы на одноразовые номера. Для входа в аккаунт с другого устройства необходимо ввести одноразовый код, получить его по SMS возможности уже нет. Чтобы не потерять доступ, создана эта утилита. Она позволяет хранить сессии в зашифрованном виде и посмотреть последнее сообщение от Telegram, в котором указан код для аутентификации.\n## Использование\n### Установка\n```\npip install tg-session-keeper\n```\n### Запуск\n```\nusage: __main__.py [-h] [--filename FILENAME] [--test]\n\noptional arguments:\n  -h, --help           show this help message and exit\n  --filename FILENAME  path to a sessions file\n  --test               run keeper on test Telegram server\n```\n### Команды\n```\nadd                создать Telegram-сессию\nremove <NUMBER>    удалить сессию\nlist               список сессий\nget <NUMBER>       посмотреть последнее сообщение от Telegram\nexit               выйти из программы\n```\n## Скриншоты\n### Список сессий\n![Список сессий](https://github.com/DavisDmitry/tg-session-keeper/raw/master/img/sessions.png)\n### Пример сообщения от Telegram\n![Сообщение от Telegram](https://github.com/DavisDmitry/tg-session-keeper/raw/master/img/message.png)\n',
    'author': 'Dmitry Davis',
    'author_email': 'dmitrydavis@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DavisDmitry/tg-session-keeper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

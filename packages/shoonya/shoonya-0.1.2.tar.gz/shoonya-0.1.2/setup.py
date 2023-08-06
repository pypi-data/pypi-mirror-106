# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shoonya']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'shoonya',
    'version': '0.1.2',
    'description': 'Unofficial Trading APIs for Finvasia Shoonya Platform, help for algo traders',
    'long_description': '# [shoonya](https://gitlab.com/algo2t/shoonya)\n\nUnofficial Trading APIs for Finvasia Shoonya Web Platform.\n\n[Finvasia](https://finvasia.com) offers Zero Brokerage trading and is doing good recently with it\'s new Shoonya platform.  \nPlease check [shoonya](https://shoonya.finvasia.com) web platform.  \nOpen account with [Finvasia](https://finvasia.com)\n\n**WORK IS STILL IN PROGRESS**\n\n**USE AT YOUR OWN RISK**\n\n## Installation\n\n- Python version `>3.9` is needed for this module to work\n- Git is required for below command to work\n- `pip install git+https://gitlab.com/algo2t/shoonya.git`\n\n## Alternate way\n\n- Download the `.whl` file from releases section\n- Using pip to install => `python -m pip install shoonya-0.1.0-py3-none-any.whl`\n\n## How to setup a good environment\n\n- Install latest Python version 3.9.x, download it from [here](https://www.python.org/downloads/)\n- Linux comes with python upgrade it to latest version 3.9.x\n- Use [scoop](https://scoop.sh) for Windows as package manager.\n- Use your favorite editor like [VSCodium](https://vscodium.com/) or [VSCode](https://code.visualstudio.com/) download it from [here](https://code.visualstudio.com/Download)\n- VScode is available for Windows, Linux and Mac\n- Python extension for vscode is [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python)\n- MagicPython is also good extension\n- Wonderful documentation for working with python and vscode is [here](https://code.visualstudio.com/docs/languages/python)\n- Use virtualenv to create a virtual python env so that your system is not affected\n- Steps for virtualenv creation - `python -m pip install virtualenv` and then virtualenv venv\n- Activate the `venv` => `.\\venv\\Scripts\\activate` (this is an example for Windows OS)\n- Install and upgrade modules `(venv) PS D:\\trading\\algo2trade\\shoonya> python -m pip install -U pip wheel setuptools pylint rope autopep8`\n\n## Usage\n\n```python\n# Check config.py example FIRST\n\nfrom config import username, password, panno\n\nfrom shoonya import Shoonya\n\naccess_params = Shoonya.login_and_get_authorizations(username=username, password=password, panno=panno)\n\nprint(access_params)\nwith open(\'params.json\', \'w\') as wrl:\n    json.dump(access_params, wrl)\n\n```\n\n## `config.py` example\n\n```python\n\nusername=\'FA12345\'\npassword=\'FinvAsia@P123\'\npanno=\'ABCDE1234Z\'\n\n```\n\n## Usage existing `params.json`\n\n```python\n\nimport json\nfrom config import username, password, panno\n\nfrom shoonya import Shoonya, TransactionType, ProductType, OrderType, InstrumentType\n\n\n# NOTE: The params.json is created using the above login example\n\nACCESS_FILE = f\'params.json\'\nwith open(ACCESS_FILE, "r") as access:\n    credentials = json.load(access)\n    access_token = credentials["access_token"]\n    key = credentials[\'key\']\n    token = credentials["token_id"]\n    username = credentials[\'user_id\']\n    usercode = credentials["usercode"]\n    usertype = credentials["usertype"]\n    panno = credentials[\'panno\']\n\nshn = Shoonya(username, access_token, panno, key,\n              token, usercode, usertype, master_contracts_to_download=[\'NSE\', \'NFO\'])\n\nbal = shn.get_limits()\nprint(bal)\ndf = pd.DataFrame(bal, index=None)\ndf[\'MTM\'] = df[\'REALISED_PROFITS\'] + df[\'MTM_COMBINED\']\nprint(df[[\'MTM\',\'REALISED_PROFITS\', \'AMOUNT_UTILIZED\',\n      \'CLEAR_BALANCE\', \'AVAILABLE_BALANCE\', \'MTM_COMBINED\']])\n\nscrip = shn.get_instrument_by_symbol(\'NSE\', \'SBIN\')\nprint(scrip)\n\n\n```\n\n## Check complete example in examples folder\n\n- [Here](https://gitlab.com/algo2t/shoonya/-/blob/main/examples/) `using_existing_access_tokens.py` is present for help\n',
    'author': 'Algo 2 Trade',
    'author_email': 'help@algo2.trade',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

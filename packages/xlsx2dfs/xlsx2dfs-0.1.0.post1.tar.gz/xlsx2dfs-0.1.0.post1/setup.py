# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xlsx2dfs']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2.4,<2.0.0']

setup_kwargs = {
    'name': 'xlsx2dfs',
    'version': '0.1.0.post1',
    'description': 'Read and write list of `pandas.DataFrame`s of tabular data from/to excel file.',
    'long_description': '\n# xlsx2dfs\n\n## Installation\n\nInstall by:\n```bash\npip install xlsx2dfs\n```\nAlternatively:\n```bash\npip install -e \'git+https://gwangjinkim@bitbucket.org/gwangjinkim/xlsx2dfs.git#egg=xlsx2dfs\'\n```\n\n## Usage\n\n`xlsx2dfs` reads a xlsx file with different sheets and tables as pandas data frame\nand a list of sheet_names.\n\n```python\nfrom xlsx2dfs import xlsx2dfs, withNames, dfs2xlsx\n```\nset test file name/path\n```python\nfpath = "test.xlsx"\n```\nread into list of data frames and list of names\n```python\ndfs, sheet_names = xlsx2dfs(fpath)\n```\nwrite a list of data frames and sheet_names into a file\n```python\nout_fpath = "out_test.xlsx"\ndfs2xlsx(withNames("sheet1", dfs[0], "sheet2" dfs[1], "sheet3", dfs[2]), out_fpath)\n```\ndocument the version:\n\n- Linux: `$ pip freeze | grep xlsx2dfs`\n- Windows: `c:\\> pip freeze | findstr xlsx2dfs`\n\n\n',
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': 'Gwang-Jin Kim',
    'maintainer_email': 'gwang.jin.kim.phd@gmail.com',
    'url': 'https://bitbucket.org/gwangjinkim/xlsx2dfs/src',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)

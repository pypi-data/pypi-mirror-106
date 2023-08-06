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
    'version': '0.1.0.post6',
    'description': 'Read and write list of `pandas.DataFrame`s of tabular data from/to excel file.',
    'long_description': '\n# xlsx2dfs\n\nEasy loading from and writing to excel sheets to/from pandas DataFrames (and list of sheet_names).\n\n\n## Installation\n\n```bash\npip install xlsx2dfs\n```\n\n## Usage\n\n```python\nfrom xlsx2dfs import xlsx2dfs, withNames, dfs2xlsx\n\n# xlsx file path\nfpath = "test.xlsx"\n\n# read from it:\ndfs, sheet_names = xlsx2dfs(fpath)\n\n# write to it \nout_fpath = "out_test.xlsx"\ndfs2xlsx(dfs, sheet_names=["sheet1", "sheet2", "sheet3"], out_fpath=out_fpath)\n\n# or using `withNames` which allows alternate input of sheet_name and corresponding df\n# `withNames("sheet1", dfs[0], "sheet2" dfs[1], "sheet3", dfs[2])` returns\n# ([dfs[0], dfs[1], dfs[2]], ["sheet1", "sheet2", "sheet3"])\n# thus (dfs, sheet_names). Using asterisk we can integrate them into the argument list\n# of `dfs2xlsx`.\ndfs2xlsx(*withNames("sheet1", dfs[0], "sheet2" dfs[1], "sheet3", dfs[2]), out_fpath)\n# This makes especially sense when you have different data frames as results in your script\n# and you want to save few lines of code which would be needed to bind them\n# together into a list and name them.\n# Instead, you can do the naming and binding to a list using `*withNames().\n# This also enhances readability and is intuitive.\n# e.g.\ndfs2xlsx(*withNames("Temperatures", temperatures_df,\n                    "Prediction", prediction_df,\n                    "Original Data", orig_df), \n         "/path/to/output/file.xlsx")\n\n\n```\n\ndocument the version:\n\n- Linux: `$ pip freeze | grep xlsx2dfs`\n- Windows: `c:\\> pip freeze | findstr xlsx2dfs`\n\n\n',
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

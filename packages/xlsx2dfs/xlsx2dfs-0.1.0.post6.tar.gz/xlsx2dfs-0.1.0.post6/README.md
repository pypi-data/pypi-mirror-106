
# xlsx2dfs

Easy loading from and writing to excel sheets to/from pandas DataFrames (and list of sheet_names).


## Installation

```bash
pip install xlsx2dfs
```

## Usage

```python
from xlsx2dfs import xlsx2dfs, withNames, dfs2xlsx

# xlsx file path
fpath = "test.xlsx"

# read from it:
dfs, sheet_names = xlsx2dfs(fpath)

# write to it 
out_fpath = "out_test.xlsx"
dfs2xlsx(dfs, sheet_names=["sheet1", "sheet2", "sheet3"], out_fpath=out_fpath)

# or using `withNames` which allows alternate input of sheet_name and corresponding df
# `withNames("sheet1", dfs[0], "sheet2" dfs[1], "sheet3", dfs[2])` returns
# ([dfs[0], dfs[1], dfs[2]], ["sheet1", "sheet2", "sheet3"])
# thus (dfs, sheet_names). Using asterisk we can integrate them into the argument list
# of `dfs2xlsx`.
dfs2xlsx(*withNames("sheet1", dfs[0], "sheet2" dfs[1], "sheet3", dfs[2]), out_fpath)
# This makes especially sense when you have different data frames as results in your script
# and you want to save few lines of code which would be needed to bind them
# together into a list and name them.
# Instead, you can do the naming and binding to a list using `*withNames().
# This also enhances readability and is intuitive.
# e.g.
dfs2xlsx(*withNames("Temperatures", temperatures_df,
                    "Prediction", prediction_df,
                    "Original Data", orig_df), 
         "/path/to/output/file.xlsx")


```

document the version:

- Linux: `$ pip freeze | grep xlsx2dfs`
- Windows: `c:\> pip freeze | findstr xlsx2dfs`



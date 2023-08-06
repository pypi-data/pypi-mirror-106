
# xlsx2dfs

## Installation

Install by:
```bash
pip install xlsx2dfs
```
Alternatively:
```bash
pip install -e 'git+https://gwangjinkim@bitbucket.org/gwangjinkim/xlsx2dfs.git#egg=xlsx2dfs'
```

## Usage

`xlsx2dfs` reads a xlsx file with different sheets and tables as pandas data frame
and a list of sheet_names.

```python
from xlsx2dfs import xlsx2dfs, withNames, dfs2xlsx
```
set test file name/path
```python
fpath = "test.xlsx"
```
read into list of data frames and list of names
```python
dfs, sheet_names = xlsx2dfs(fpath)
```
write a list of data frames and sheet_names into a file
```python
out_fpath = "out_test.xlsx"
dfs2xlsx(withNames("sheet1", dfs[0], "sheet2" dfs[1], "sheet3", dfs[2]), out_fpath)
```
document the version:

- Linux: `$ pip freeze | grep xlsx2dfs`
- Windows: `c:\> pip freeze | findstr xlsx2dfs`



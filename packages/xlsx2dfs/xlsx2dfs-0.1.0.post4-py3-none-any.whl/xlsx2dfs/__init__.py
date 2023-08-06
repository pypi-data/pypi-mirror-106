__version__ = '0.1.0'

import pandas as pd

def dfs2xlsx(dfs, sheet_names=None, outfpath="output.xlsx", **kwargs):
    """
    Write a list of DataFrames [dfs] to an Excel file [outfpath]
    with Sheet names given in [sheet_names].
    
    Parameters:
      dfs : DataFrames list
      outfpath : Output file path
                 (Example: '/path/to/file.xlsx')
      sheet_names : Names of sheets for each DataFrame.
      **kw_args : other arguments passed to the excel writer in Pandas

    Returns: None
    """
    if sheet_names is None:
        sheet_names = ["Sheet" + str(i) for i in range(len(dfs))]
    with pd.ExcelWriter(outfpath, engine='openpyxl') as writer:    
        for i, df in enumerate(dfs):
            df.to_excel(writer, sheet_names[i], **kwargs)
        writer.save()

def withNames(*args):
    """
    Helper function to input: "Sheet_1", DataFrame_1, "Sheet_1", DataFrame_2, ...
    for dfs2xlsx(). And it will output (dfs, sheetnames) so that one can put
    it into parameter with asterisk.
    dfs2xlsx(*withNames("Sheet1", df1, "Sheet2", df2, ...),
             outfpath="test.xlsx")
    Parameters:
      *args: alternating string (sheet_name) and DataFrame
    
    Returns: DataFrames list, sheet_names (strings list)
    """
    assert len(args) % 2 == 0, "Non even number of args!"
    gen = (x for x in args)
    sheet_names, dfs = [], []
    for _ in range(int(len(args) / 2)):
        sheet_names.append(next(gen))
        dfs.append(next(gen))
    return dfs, sheet_names

def xlsx2dfs(fpath, header=None, index_col=None, **kwargs):
    """
    Read Excel Sheets of an Excel file [fpath] into a list of DataFrames.
    The assumption is that the Excel Sheets contain pandas-readable DataFrame data.
    
    Parameters:
      fpath : Input Excel file path
      header, index_col, **kwargs : parameters passed to pd.read_excel() function
    
    Returns: Tuple of list of pandas data frames, list of sheet names
    """
    xls = pd.ExcelFile(fpath)
    dfs = [ pd.read_excel(fpath, header=header, index_col=index_col, sheet_name=x, **kwargs) \
             for x in xls.sheet_names]
    return dfs, xls.sheet_names


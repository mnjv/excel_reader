from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Any, Dict, List
import pandas as pd

Row = Dict[str, Any]

@dataclass_json
@dataclass
class Sheet:
    name: str
    rows: List[Row]

@dataclass_json
@dataclass
class Workbook:
    name: str
    sheets: List[Sheet]

def read_excel(filepath: str) -> Workbook:
    # Read all sheets from excel file into a dict of dataframes
    xls = pd.ExcelFile(filepath)
    sheets = []
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        # Convert dataframe rows to list of dicts
        rows = df.to_dict(orient='records')
        sheets.append(Sheet(name=sheet_name, rows=rows))
    return Workbook(name=filepath, sheets=sheets)

def read_csv(filepath: str) -> Sheet:
    df = pd.read_csv(filepath)
    rows = df.to_dict(orient='records')
    # Use the filename as the sheet name (without extension)
    import os
    sheet_name = os.path.splitext(os.path.basename(filepath))[0]
    return Sheet(name=sheet_name, rows=rows)


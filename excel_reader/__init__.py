# excel_reader/__init__.py
## This makes it possible to do `from <library> import greet` instead of `from <library>.core import greet`
from .core import Row, Sheet, Workbook, read_excel, read_csv

__version__ = "0.1.0"
__all__ = ["Row", "Sheet", "Workbook", "read_excel", "read_csv"]

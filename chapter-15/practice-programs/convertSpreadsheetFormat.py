#! python3
# convertSpreadsheetFormat.py - Downloads uploaded spreadsheet in multiple formats

import ezsheets

ss = ezsheets.upload('[spreadsheetFile]')

ss.downloadAsExcel()
ss.downloadAsODS()
ss.downloadAsCSV()
ss.downloadAsTSV()
ss.downloadAsPDF()
ss.downloadAsHTML()
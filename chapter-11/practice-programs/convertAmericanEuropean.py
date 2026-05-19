#! python3
# convertAmericanEuropean.py - Converts American Dates present in file names to European Dates

import shutil, re, os
from pathlib import Path

def americanEuropeanDates(folderPath):
    for folder_name, subfolders, filenames in os.walk(folderPath):
        for filename in filenames:
            dateMatch = re.match(r"([a-zA-Z]+)([0-9]{2})-([0-9]{2})-([0-9]{4}).([a-zA-Z]+)", filename)
            if dateMatch == None:
                continue
            else:
                month = dateMatch.group(2)
                day = dateMatch.group(3)
                year = dateMatch.group(4)
                orgFileName = Path(folder_name) / filename
                newFileName = Path(folder_name) / f'{dateMatch.group(1)}{day}-{month}-{year}.{dateMatch.group(5)}'

            print(f'Renaming "{orgFileName}" to "{newFileName}')
            shutil.move(orgFileName, newFileName)

americanEuropeanDates(Path.cwd())

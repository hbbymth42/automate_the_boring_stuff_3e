#! python3
# regexSearch.py - Searches for any line in a text file that matches a user-supplied regular expression
import re
from pathlib import Path

directory = Path(Path.cwd() / 'testDir/')
print('Enter a Regular Expression for Search:')
searchRegex = input()


for textFilePath in directory.glob('*.txt'):
    textLines = open(textFilePath).readlines()
    for line in textLines:
        result = re.search(f"{searchRegex}", line)
        if result:
            print(f'Result found: {line}\n')
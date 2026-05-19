#! python3
# fillGaps.py - Fill in gaps for filenames in directory

import shutil, re, os
from pathlib import Path

def fillInGaps(folderPath):
    iteratorNum = 1
    for fileName in sorted(os.listdir(folderPath)):
        fileNameMatch = re.findall("[a-zA-Z\\.0]+|[1-9]?",fileName)
        
        beforePart = fileNameMatch[0]
        numPart = fileNameMatch[1]
        fileExtenPart = fileNameMatch[2]

        if int(numPart) == iteratorNum:
            iteratorNum = iteratorNum + 1
            continue
        else:
            numPart = int(numPart)
            numPart = iteratorNum

            newFileName = beforePart + str(numPart) + fileExtenPart

            absWorkingDir = os.path.abspath(folderPath)
            orgFileName = os.path.join(absWorkingDir, fileName)
            newFileName = os.path.join(absWorkingDir, newFileName)

            print(f'Renaming "{orgFileName}" to "{newFileName}"...')
            shutil.move(orgFileName, newFileName)
            iteratorNum = iteratorNum + 1


fillInGaps(Path.cwd() / 'testFiles')

#! python3
# insertGaps.py - Insert gaps for filenames in directory

import shutil, re, os
from pathlib import Path

def insertGaps(folderPath, gapNum = 0):
    iteratorNum = len(os.listdir()) + 1
    for fileName in sorted(os.listdir(folderPath), reverse=True):
        fileNameMatch = re.findall("[a-zA-Z\\.0]+|[1-9]?",fileName)
        
        beforePart = fileNameMatch[0]
        numPart = fileNameMatch[1]
        fileExtenPart = fileNameMatch[2]

        if int(numPart) == gapNum:
            numPart = int(numPart)
            numPart = numPart + 1
            newFileName = beforePart + str(numPart) + fileExtenPart

            absWorkingDir = os.path.abspath(folderPath)
            orgFileName = os.path.join(absWorkingDir, fileName)
            newFileName = os.path.join(absWorkingDir, newFileName)

            print(f'Renaming "{orgFileName}" to "{newFileName}"...')
            shutil.move(orgFileName, newFileName)
            iteratorNum = iteratorNum - 2
            continue

        if int(numPart) == iteratorNum:
            iteratorNum = iteratorNum - 1
            continue
        else:
            numPart = int(numPart)
            if iteratorNum == 0:
                continue
            numPart = iteratorNum

            newFileName = beforePart + str(numPart) + fileExtenPart

            absWorkingDir = os.path.abspath(folderPath)
            orgFileName = os.path.join(absWorkingDir, fileName)
            newFileName = os.path.join(absWorkingDir, newFileName)

            print(f'Renaming "{orgFileName}" to "{newFileName}"...')
            shutil.move(orgFileName, newFileName)
            iteratorNum = iteratorNum - 1


insertGaps(Path.cwd() / 'testFiles', 4)

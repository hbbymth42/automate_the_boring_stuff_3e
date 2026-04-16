#! python3
# selectiveCopy.py - Walks through a folder tree and searches for files with a certain file extension, and copies these files from their location to a new folder

from pathlib import Path
import os, shutil

def selectiveCopy(sourceFolder, destinationFolder, fileExtension):
    if not os.path.exists(destinationFolder):
        os.mkdir(destinationFolder)
    for foldername, subfolders, filenames in os.walk(sourceFolder):
        print(f'Adding files to {destinationFolder}')
        for filename in filenames:
            if filename.endswith(fileExtension):
                shutil.copy(os.path.join(foldername,filename),os.path.join(destinationFolder,filename))


selectiveCopy(Path.home() / 'Documents/Projects/Project_Tutorials/Automate_The_Boring_Stuff_2nd_Edition/chapter-9/practice-projects', Path.cwd() / 'chapter-9-pps', '.py')

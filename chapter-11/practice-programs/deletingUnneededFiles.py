#! python3
# deletingUnneededFiles.py - Walks through a folder tree and searches for exceptionally large files, then prints absolute path of files to the screen.

from pathlib import Path
import os, shutil

def filesToDelete(path, fileSize):

    path = os.path.abspath(path)
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if os.path.getsize(f'{foldername}/{filename}') > fileSize:
                print(f'To Delete - File exceeds {int(fileSize / 1000)}KB - Path: {foldername}/{filename}')


filesToDelete(Path.home() / 'Documents/Projects/Project_Tutorials/learn_to_program_with_assembly', 1000)

#! python3 
# photoFoldersOnDrive.py - Finds potential photo folders across the user's computer

import os
from PIL import Image
from pathlib import Path

for foldername, subfolders, filenames in os.walk(Path.home()):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not(filename.lower().endswith('.png') or filename.lower().endswith('jpg')):
            numNonPhotoFiles += 1
            continue
        try:
            im = Image.open(os.path.join(foldername,filename))
            width, height = im.size

            if width > 500 and height > 590:
                numPhotoFiles += 1
            else:
                numNonPhotoFiles += 1
        except:
            numNonPhotoFiles += 1
            continue

    if numPhotoFiles > (numNonPhotoFiles + numPhotoFiles) / 2:
        print(f'Photo Folder Found!: {os.path.abspath(foldername)}')
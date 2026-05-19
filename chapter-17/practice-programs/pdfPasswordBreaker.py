#! python3
# pdfPasswordBreaker.py - Breaks password encryption for PDF Files (Brute-Force Method)

import pypdf
from pathlib import Path

dictionaryFile = open(Path.cwd() / 'dictionary.txt')

wordList = dictionaryFile.readlines()

for word in wordList:
    noNewLineWord = word.rstrip('\n')
    pdfReader = pypdf.PdfReader('watermark_encrypted.pdf')
    if pdfReader.decrypt(noNewLineWord.upper()).name == 'NOT_DECRYPTED':
        pdfReader = pypdf.PdfReader('watermark_encrypted.pdf')
        if pdfReader.decrypt(noNewLineWord.lower()).name == 'NOT_DECRYPTED':
            continue
        else:
            print(f'Password found!: {noNewLineWord.lower()}')
            break
    else:
        print(f'Password found!: {noNewLineWord.upper()}')
        break

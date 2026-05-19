#! python3
# pdfParanoiaDecrypt.py - Decrypt all Encrypted PDFs in folder

import pypdf, os, re, sys

folder = './pdf-files'

folder = os.path.abspath(folder)

passwordGuess = ''

for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        pdfReader = pypdf.PdfReader(os.path.join(folderName, filename))
        if pdfReader.is_encrypted == False:
            continue
        print('Please enter password for this PDF: ')
        passwordGuess = input()
        if pdfReader.decrypt(passwordGuess).name == 'NOT_DECRYPTED':
            print('Incorrect Password, continuing to next PDF')
            continue
        else:
            pdfWriter = pypdf.PdfWriter()
            pdfWriter.append(pdfReader)
            decryptFilename = str(re.findall(r'[\w\d]+|[\.]', filename)[0]) + '_decrypted.pdf'
            with open(os.path.join(folderName, decryptFilename), 'wb') as file:
                pdfWriter.write(file)
print('Done.')

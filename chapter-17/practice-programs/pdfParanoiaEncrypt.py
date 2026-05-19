#! python3
# pdfParanoiaEncrypt.py - Encrypt all PDFs in folder

import pypdf, os, re, sys

PASSWORD = sys.argv[1]

folder = './pdf-files'

folder = os.path.abspath(folder)

for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        pdfReader = pypdf.PdfReader(os.path.join(folderName, filename))
        if pdfReader.is_encrypted:
            continue
        pdfWriter = pypdf.PdfWriter()
        pdfWriter.append(pdfReader)
        pdfWriter.encrypt(PASSWORD, algorithm='AES-256')
        encryptFilename = str(re.findall(r'[\w\d]+|[\.]', filename)[0]) + '_encrypted.pdf'
        with open(os.path.join(folderName, encryptFilename) , 'wb') as file:
            pdfWriter.write(file)
        encryptPdfReader = pypdf.PdfReader(os.path.join(folderName, encryptFilename))
        if encryptPdfReader.is_encrypted:
            os.remove(os.path.join(folderName, filename))
        else:
            print('Not encrypted')

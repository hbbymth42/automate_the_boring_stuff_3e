# combine_pdfs.py - Combines all the PDFs in the current working directory into a single PDF

import pypdf, os

# Get all the PDF filenames.
pdf_filenames = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_filenames.append(filename)
pdf_filenames.sort(key=str.lower)

writer = pypdf.PdfWriter()

# Loop through all the PDF files.
for pdf_filename in pdf_filenames:
    reader = pypdf.PdfReader(pdf_filename)
    # Copy all pages after the first page.
    writer.append(pdf_filename, (1, len(reader.pages)))

# Save the resulting PDF to a file.
with open('combined.pdf', 'wb') as file:
    writer.write(file)

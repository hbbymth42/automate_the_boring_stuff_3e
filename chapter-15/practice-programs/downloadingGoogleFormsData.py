#! python3
# downloadingGoogleFormsData.py - Downloads Google Forms Data

import ezsheets

ss = ezsheets.Spreadsheet('[spreadsheetIDforGoogleFormResponses]')

emailList = []

responseSheet = ss[0]

for i in range(2, responseSheet.rowCount):
    if responseSheet[3, i] == '':
        continue
    else:
        emailList.append(responseSheet[3, i])

print(emailList)
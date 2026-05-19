#! python3
# findingMistakes.py - Find Mistake in Spreadsheet Totals

import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

for i in range(2, ss[0].rowCount):
    try:
        if int(ss[0].getRow(i)[0]) * int(ss[0].getRow(i)[1]) != int(ss[0].getRow(i)[2]):
            print(f'Incorrect Total on Row Number: {i}')
    except:
        continue
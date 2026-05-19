#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the words ADJECTIVE, NOUN, ADVERB or VERB appear in the text file.

from pathlib import Path
import re

madLibFile = open(Path.cwd() / 'test.txt')
fileLines = madLibFile.readlines()
madLibFile.close()

for i in range(len(fileLines)):
    sentenceList = re.findall(r"[\w]+|[\s]|[\.]", fileLines[i])
    finalSentence = []
    for word in sentenceList:
        if word == 'ADJECTIVE':
            print('Enter an adjective:')
            adjective = input()
            finalSentence.append(adjective)
        elif word == 'NOUN':
            print('Enter an noun:')
            noun = input()
            finalSentence.append(noun)
        elif word == 'ADVERB':
            print('Enter an adverb:')
            adverb = input()
            finalSentence.append(adverb)
        elif word == 'VERB':
            print('Enter an verb:')
            verb = input()
            finalSentence.append(verb)
        else:
            finalSentence.append(word)
    print("".join(finalSentence))
    if i == 0:
        newFile = open(Path.cwd() / 'testMadLib.txt', 'w')
        newFile.write(''.join(finalSentence))
        newFile.close()
    else:
        newFile = open(Path.cwd() / 'testMadLib.txt', 'a')
        newFile.write(''.join(finalSentence))
        newFile.close()

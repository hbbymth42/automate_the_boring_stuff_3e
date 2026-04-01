import re

def regexStrip(text, removeChars = ''):
    if removeChars == '':
        strippedMatches = []
        nonRemoveRegex = re.compile(r'([\S]+)')
        spaceRegex = re.compile(r'([\s]+)')
        charMatches = nonRemoveRegex.findall(text)
        spaceMatches = spaceRegex.findall(text)
        if len(spaceMatches) < len(charMatches):
            return text
        if text[0] == ' ' and text[-1] == ' ':
            for i in range(len(charMatches)):
                strippedMatches.append(charMatches[i])
                if i < (len(charMatches) - 1):
                    strippedMatches.append(spaceMatches[i+1])
            return ''.join(strippedMatches)
        elif text[0] == ' ':
            for i in range(len(charMatches)):
                strippedMatches.append(charMatches[i])
                if i < (len(charMatches) - 1):
                    strippedMatches.append(spaceMatches[i+1])
            return ''.join(strippedMatches)
        elif text[-1] == ' ':
            for i in range(len(charMatches)):
                strippedMatches.append(charMatches[i])
                if i < (len(charMatches) - 1):
                    strippedMatches.append(spaceMatches[i])
            return ''.join(strippedMatches)
    else:
        removeRegex = re.compile(f'[^{removeChars}]+')
        charMatches = removeRegex.findall(text)
        return ''.join(charMatches)

test1 = 'Test Text... This is a Test'
test2 = 'Test Text... This is a Test  '
test3 = '  Test Text... This is a Test'
test4 = '  Test Text... This is a Test  '
print(regexStrip(test1))
print(regexStrip(test2))
print(regexStrip(test3))
print(regexStrip(test3))
print(regexStrip(test1, 'T'))
print(regexStrip(test1, 'e'))
print(regexStrip(test1, 's'))
print(regexStrip(test1, 't'))

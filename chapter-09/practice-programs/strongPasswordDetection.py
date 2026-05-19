import re

def strongPassword(pword):
    upperCaseRegex = re.compile(r'[A-Z]+')
    lowerCaseRegex = re.compile(r'[a-z]+')
    digitRegex = re.compile(r'\d+')
    if len(pword) > 8:
        if len(upperCaseRegex.findall(pword)) > 0:
            if len(lowerCaseRegex.findall(pword)) > 0:
                if len(digitRegex.findall(pword)) > 0:
                    print('Strong Password')
                else:
                    print('Weak Password')
            else:
                print('Weak Password')
        else:
            print('Weak Password')
    else:
        print('Weak Password')

password = "Test%#@1a"
strongPassword(password)

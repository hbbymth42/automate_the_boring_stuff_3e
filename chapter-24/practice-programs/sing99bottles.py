import pyttsx3, time

iterator = 99

while iterator > 0:
    if iterator == 1:
        pyttsx3.speak(f'{iterator} bottle of beer on the wall,')
        pyttsx3.speak(f'{iterator} bottle of beer,')
        pyttsx3.speak('Take one down, pass it around,')
        iterator = iterator - 1
        pyttsx3.speak('No more bottles of beer on the wall.')
    elif iterator == 2:
        pyttsx3.speak(f'{iterator} bottles of beer on the wall,')
        pyttsx3.speak(f'{iterator} bottles of beer,')
        pyttsx3.speak('Take one down, pass it around,')
        iterator = iterator - 1
        pyttsx3.speak(f'{iterator} bottle of beer on the wall.')
        time.sleep(1)
    else:
        pyttsx3.speak(f'{iterator} bottles of beer on the wall,')
        pyttsx3.speak(f'{iterator} bottles of beer,')
        pyttsx3.speak('Take one down, pass it around,')
        iterator = iterator - 1
        pyttsx3.speak(f'{iterator} bottles of beer on the wall.')
        time.sleep(1)

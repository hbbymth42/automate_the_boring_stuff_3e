def comma_code(word_list):
    sentence = ''
    for i, word in enumerate(word_list):
        if i == len(word_list) - 1:
            sentence += 'and ' + word
        else:
            sentence += word + ', '
    return sentence

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))

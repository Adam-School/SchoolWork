#This final project will be a story from the throne of glass series.

firstN = ''
LastN = ''
fullN = ''

def main():
    print('This story is about you and your life... What I need to ask of you is would you please remind me what you name is.')
    globals()['firstN'] = raw_input('Please enter your first name: ')
    globals()['lastN'] = raw_input('Please enter your last name: ')
    globals()['fullN'] = firstN + ' ' + lastN
    print('')
    print('Ah yes I remember you and the legend that you left behind... What you dont remember what you did do you?')
    remember = raw_input('Do you remember what your story is ? (Y or N)')
    print('')
    if remember.upper() == 'Y':
        print('Well then im going to say your legend anyways for the children that have gathered around us. ')
        print('')
    elif remember.upper() == 'N':
        print('Well grab a seat ill be sharing your legend with the kids that have gathered and ill refreash your memory')
        print('')
    else:
        print('What language did you speak in I have no idea what you have said. But regardless im going to tell your legend.')
        print('')

    print('And so your legend '+ fullN + ' starts off in the lowest time in your life.')
    print('')
    starting()
    restart()


def starting():

    with open('begining.txt') as f:
        newText=f.read().replace('youu', fullN)
    with open('begining.txt', 'w') as f:
        f.write(newText)
    with open('begining.txt') as f:
        newTexts=f.read().replace('uuu', firstN)
    with open('begining.txt', 'w') as f:
        f.write(newTexts)
    f.close()

    f = open('begining.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

def restart():
    with open('begining.txt') as f:
        newText=f.read().replace(fullN, 'youu')
    with open('begining.txt', 'w') as f:
        f.write(newText)
    with open('begining.txt') as f:
        newTexts=f.read().replace(firstN ,'uuu')
    with open('begining.txt', 'w') as f:
        f.write(newTexts)
    f.close()
main()

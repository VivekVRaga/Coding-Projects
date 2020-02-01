import re, pyperclip


def strength(passw):
    # determine whether password strength is sufficint
    # must be at least 8 charaters long
    # must have upper and lowercase characters
    # must have at least one digit

    digitRegex = re.compile(r'\d')

    if len(passw) < 8:
        return False
    elif passw.upper() == passw:
        return False
    elif digitRegex.search(passw) == '':
        return False
    else:
        return True


text = input('type in example text here \n')

if strength(text) == True:
    print('stronk')
else:
    print('not')

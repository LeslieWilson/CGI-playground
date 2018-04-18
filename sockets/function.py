

def fortune():
    input = raw_input('Do you like blue or green? Ill tell you your fortune (b/g)')
    if input == 'b':
        return " you will die in a horrible car accident "
    elif input == 'g':
        return "you will marry a rich daughter"
    else:
        return "you need to put the correct letters in"


"""
Leslie Wilson
April 18, 2018
function.py

Summary: this is the function I'm calling from the client side. It would be
messy to have this in the client code so I wanted to practice importing it in.
It takes a simple input and spits out a response (a fortune)
"""

def fortune():
    input = raw_input('Do you like blue or green? Ill tell you your fortune (b/g)')
    if input == 'b':
        return " you will die in a horrible car accident "
    elif input == 'g':
        return "you will marry a rich daughter"
    else:
        return "you need to put the correct letters in"

# I don't do main() here because I don't want it randomly running the function
# before I want it to. I also don't use print statements because I want to
# use this information and move it around, so I used returns.

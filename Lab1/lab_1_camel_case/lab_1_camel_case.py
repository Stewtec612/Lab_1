'''
Convert any sentence entered as camel case
The first word is not capitalized 
and the other words are capitalized and no spaces in-between

'''

from re import sub



def banner():
    """Display program name"""
    message = 'Awesome camel case program!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

#function converts the user's input into a camelCase format
def camilize(userInput):

    
    userInput = sub(r"(_|-)+"," ", userInput).title().replace(" ", "")
    return ''.join([userInput[0].lower(), userInput[1:]])

def main():
    banner()
    print('Convert any sentence into camelCase')

    userInput = input('Enter a sentence: ')

    print(camilize(userInput))

main()









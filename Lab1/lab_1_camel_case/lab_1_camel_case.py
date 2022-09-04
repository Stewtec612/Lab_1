'''
Convert any sentence entered as camel case
The first word is not capitalized 
and the other words are capitalized and no spaces in-between

'''

from re import sub





#function converts the user's input into a camelCase format
def camilize(userInput):

    
    userInput = sub(r"(_|-)+"," ", userInput).title().replace(" ", "")
    return ''.join([userInput[0].lower(), userInput[1:]])

def main():

    print('Convert any sentence into camelCase')

    userInput = input('Enter a sentence: ')

    camel_case = camilize(userInput)

    print(camel_case)

main()









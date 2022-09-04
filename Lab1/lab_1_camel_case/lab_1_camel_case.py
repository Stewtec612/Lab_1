'''
Convert any sentence entered as camel case
The first word is not capitalized 
and the other words are capitalized and no spaces in-between

'''

from re import sub



#function converts the user's input into a camelCase format
def camilize(user_input):

    
    user_input = sub(r"(_|-)+"," ", user_input).title().replace(" ", "")
    return ''.join([user_input[0].lower(), user_input[1:]])

def main():

    print('Convert any sentence into camelCase')
    user_input = ('insert sentence you want to convert to camel case: ')

    camel_case = camilize(user_input)

    print(camel_case)
    
main()









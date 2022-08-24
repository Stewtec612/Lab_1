
''' 
Hello, Birthday Month

This program will ask for your name and your month of birth

The program will respond with a greeting with your name 
 and respond with how many letters are in your name

then, depending on the month entered, 
the program will say "Happy Birthday!" if the current month is the same 
'''

from datetime import date, datetime

#list of months so program can put a name to the month number
#months = ['January', 'Febuary','March','April','May','June','July','August',
#'September', 'October', 'November','December']


print('Hello!')

print('Please enter your name:')
username = input()
print('Hello ' + username + '!')

number_of_letters = len(username)
print('there are ' + str(number_of_letters) + ' letters in your name')

print('what month were you born in, ' + username + '?')
birth_month = input()

#easier method
if birth_month == 'august':
    print('Happy Birthday, ' + username + '!')

else:
    print('I am excited for ' + birth_month + '!')

#harder method
current_time = datetime.now()
print('what is your birthday month(numerical),  ' + username + '?' )

#for month in months:
   # print(month)

month_of_birth = int(input())

current_month = current_time.month
print(current_month)

if month_of_birth == current_month:
    print('happy birthday, ' + username + '!')

else:
    print('see you until then!')


'''
List of Classes

Ask what classes you are taking this semester
Then save them into a list and print the list(one per line)
'''
#create an empty list that will collect each class entered
classes = []

print('List of Classes')
#set the amount of items that will load into a list
n = int(input("Enter number of elements in the list : "))

#set the range so you will be asked as many times as you entered
for i in range(0 , n):
    str(print ('Class-{}:'.format(i+1)))
    elm = str(input())
    classes.append(elm)

#once you have completed the number of entries, print the finished list

print('Your classes are:')
for c in classes:
    print(c)
'''
List of Classes

Ask what classes you are taking this semester
Then save them into a list and print the list(one per line)
'''
#create an empty list that will collect each class entered
classes = []

print('List of Classes')
#set the amount of items that will load into a list
num_of_classes = int(input("How many classes are you taking?: "))

#set the range so you will be asked between 1 and the amount of classes entered
for i in range(num_of_classes):
    print (f'Class-{i+1}:')
    class_name = str(input())
    classes.append(class_name)

#once you have completed the number of entries, print the finished list

print('Your classes are:')
for c in classes:
    print(c)
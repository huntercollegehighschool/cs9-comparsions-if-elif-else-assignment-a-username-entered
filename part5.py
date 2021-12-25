'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below
monthsList = ['January','February','March','April','May','June','July','August','September','October','November','December']

dayslist1 = [0,2,4,6,7,9,11]
dayslist2 = [3,5,8,10]

month = input('Enter a month: ')
month = month.capitalize()

#print(monthsList.index(month)) used in debugging

if month in monthsList:
  if monthsList.index(month) in dayslist1:
    print('31')
  elif monthsList.index(month) in dayslist2:
    print('30')
  else:
    print('28 or 29')
else:
  print('not a month')
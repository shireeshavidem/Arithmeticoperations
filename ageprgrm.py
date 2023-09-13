'''a = int(input('Tell your year of birth: '))
current_year = 2023
age = current_year-a
print('Your age is:',age)'''

#Program using datetime library
from datetime import date
a = int(input('Tell your year of birth: '))
current_year = date.today().year
age = current_year-a
print('Your age is:',age)

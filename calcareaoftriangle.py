#ask user to enter numbers and calculate area of tri
no1 = input('Enter the first number')
no2 = input('Enter the second number')
area = float(no1) * float(no2) / int(2) # no1 and no2 is str and so we need to mention data types for each numbers
print('the area of triangle is {0:.2f}'.format(area)) # {0:.2f}.format() is used because we want only 2 decimal values
 

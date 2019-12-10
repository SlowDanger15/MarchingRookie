print('----------------------------------------------------')
print('This is a program to find the factorial of a number')
print('----------------------------------------------------')
n = input('Enter a number whose factorial you want to find:')

i=1
fact=1
while i<=int(n):
    fact = fact*i
    i=i+1
print('The factorial of the number',n,'is',fact)
print('You have reached the end of the program')
print('----------------------------------------------------')

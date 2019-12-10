n = int(input('Enter a number to check whether it is an Armstrong number or not:'))
s=0
num = n
while n>0:
    rem = n%10
    s = s + rem*rem*rem
    n=int(n/10)
if s == num:
    print('ARMSTRONG NUMBER')
else:
    print('NOT ARMSTRONG NUMBER')

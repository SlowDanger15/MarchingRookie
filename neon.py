#A number is said to be a Neon Number if the sum of digits of the square of the number is equal to thenumber itself.
# Example 9 is a Neon Number. 9*9=81 and 8+1=9.Hence it is a Neon Number.
n = int(input('Enter a number to check whether it is a neon number or not: '))
num=n
s=0
sq=n*n
while sq>0:
    r=sq%10
    s=s+r
    sq=int(sq/10)

if s==num:
    print('NEON NUMBER')
else:
    print('NOT NEON NUMBER')

#An automorphic number is a number which is present in the last digit(s) of its square.
# Example: 25 is an automorphic number as its square is 625 and 25 is present as the last digits.
n = int(input('Enter a number to check whether it is automorphic or not:'))
sq = n*n

flag = 1
d=10
num=n
while True:
     r=sq%d
     if n==r:
         flag = 1
         break
     d=d*10

if flag==1:
    print('AUTOMORPHIC NUMBER')
elif flag==0:
    print('NOT AUTOMORPHIC NUMBER')
else:
    print('NOT AUTOMORPHIC NUMBER')

#A number is said to be a Magic number if the sum of its digits are calculated till a single digit is obtained by recursively adding the sum of its digits.
#If the single digit comes to be 1 then the number is a magic number.
n = int(input('Enter a number to check whether it is a magic number or not:'))
lst = []
flag = 0
num = n
while True:
    s=0
    while num>0:
        r=num%10
        s=s+r
        num=int(num/10)
        #guardian condition:
    if s in lst:
        break

    if s==1:
        flag=1
        break
    else:
        num=s
    lst.append(s)

if flag==1:
    print('MAGIC NUMBER')
else:
    print('NOT MAGIC NUMBER')

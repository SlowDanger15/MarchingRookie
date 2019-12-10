num=int(input('Enter a number to check whether a number is happy or not'))
lst = list()
lst.append(num)
flag = 0
n= num
while True:
    sum=0
    while n>0:
        r=n%10
        sum=sum+r*r
        n=int(n/10)
    if sum in lst:
        break
    if sum==1:
        flag = 1
        break
    else:
        n = sum
    lst.append(sum)
if flag==1:
    print('HAPPY NUMBER')
else:
    print('UNHAPPY NUMBER')

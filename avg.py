l = list()#creating an empty list
#program to find average using lists
#and we are also printing the list
while True:
    x = input('Enter a  value: ')
    if x == 'done': break
    f = float(x)
    l.append(f)#appending the floated value to the list

avg = sum(l)/len(l)
print(l)
print(avg)

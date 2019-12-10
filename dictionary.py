#we are gonna study dictionaries
names = ['Rohan','Dhruv','Hari','Rohan','Mitul','Hari']
count = dict()
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1

print(count)

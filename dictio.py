names = ['Rohan','Dhruv','Hari','Rohan','Mitul','Hari']
count = dict()
for name in names:
    count[name] = count.get(name,0)+1

print(count)
#using get method ....it is a method for dicyionaries to put default as 0,if name doesnt exists

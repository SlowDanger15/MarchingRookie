x='I walk a lonely road'
#program to convert a string into a list of its constituent words
stuff = x.split()
print(stuff)

print(len(stuff))
#some times you can use delimiters to specify at what point you want to chop the string by using split(';')
#Take the example of    'I;walk;a;lonely;road'

x='I;walk;a;lonely;road'
abc = x.split(';')
print(abc)
#This gives the exact same output as above

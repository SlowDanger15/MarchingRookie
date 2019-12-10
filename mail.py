fname = input("Enter file name: ")
fhand = open(fname)
c = 0
for line in fhand:
    words = line.split()
    if len(words)<1:
        continue
    if words[0]!='From':
        continue
    print(words[1])
    c=c+1
print('There were',c,'lines in the file with From as the first word')

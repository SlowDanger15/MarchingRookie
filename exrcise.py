fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   line = line.strip()
   words=line.split()
   i=0
   a = range(len(words))
   for i in a:
       if words[i] in lst: continue
       lst.append(words[i])

lst.sort()
print(lst)

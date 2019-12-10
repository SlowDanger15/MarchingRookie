handle = open('venom.txt')
count=0
i=0
for line in handle:
    for i in line:
       if line[int(i)]==' ':
          count=count+1
       i=i+1
    count=count+1

print('There are ',count,' word in the lyrics')
println('End of file reached')

handle = open('welcome.txt')#openin a file....its like a portal through which we can see the contents of the file
count = 0
for line in handle:
   line = line.strip()#removeing the '\n' tht is present at the end of every line
   print(line)
   count= count+1

print('#We have reached the EOF')
print('There are ',count,' lines in this file')

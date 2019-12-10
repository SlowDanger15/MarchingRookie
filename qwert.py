print('This is ana exercise 8.4 in coursera ......regarding lists')
#Program to open a txt file , read it line by line , and and create a list of the words, then sort the words in alphabetical order
f = open('intheend.txt','r')
contents = f.read()
print(contents)
words = contents.split()
words.sort()
print(words)

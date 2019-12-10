data = open('mail.txt')
i=0;
for line in data:
    line = line.strip()
    if line.startswith('Disclaimer'): continue
    words = line.split()
    print(words)

print('This Is the END')

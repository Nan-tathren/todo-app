filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file=open(filename,'r')
    contents=file.read()
    print(contents)

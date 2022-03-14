next_file2 = open('test3.txt','a')
name = 'I like chocolate.'
next_file2.write(name)
next_file2 = open('test3.txt','r')
print(next_file2.read())


test_file = open('test.txt','a')
test_file.write('I like Grzegorz Kozak\n')
test_file.write('Also I like Czarek')
test_file = open('test.txt','r')
print(test_file.read())
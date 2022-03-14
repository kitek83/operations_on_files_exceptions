file = open('students.txt', 'r')
print(file.read())
print('############################')
descr = file.readline()
while descr != '':
    qty = file.readline()
    print(descr)
    print(float(qty))
    descr = file.readline()

file.close()
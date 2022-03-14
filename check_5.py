file = open('students.txt','r')
descr = file.readline()
while descr != '':
    qty = file.readline()
    print(descr)
    print(qty)
    descr = file.readline()
import os
def main():
    found = False
    file = open('students.txt', 'r')
    temp_file = open('temp_file.txt','w')

    search = input('Enter the name and surname you want to delete:')
    descr = file.readline()
    while descr != '':
        qty = float(file.readline())
        descr = descr.rstrip('\n')
        #qty = qty.rstrip('\n')
        if descr != search:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            found = True
        descr = file.readline()
    file.close()
    temp_file.close()

    os.remove('students.txt')
    os.rename('temp_file.txt', 'students.txt')
    if found:
        print('File was updated and record was deleted!')
    else:
        print('Searched name wasn\'t found!')


main()
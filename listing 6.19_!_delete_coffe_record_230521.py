import os
def main():
    found = False
    cof_file = open('coffee222.txt', 'r')
    temp_file = open('temp.txt', 'w')
    descr = cof_file.readline()
    search = input('Enter name of coffe to be deleted.')
    while descr != '':
        qty = cof_file.readline()
        descr = descr.rstrip('\n')
        qty = qty.strip('\n')
        if descr != search:
            temp_file.write(descr + '\n')
            temp_file.write(qty + '\n')
        else:
            found = True # I assume, that in this moment desription is deleted from the file coffe222.txt
        descr = cof_file.readline()
    cof_file.close()
    temp_file.close()
    os.remove('coffee222.txt')
    os.rename('temp.txt', 'coffee222.txt')
    if found:
        print('File was updated.')
    else:
        print('Searched coffee wasn\'t found in the file.')


main()
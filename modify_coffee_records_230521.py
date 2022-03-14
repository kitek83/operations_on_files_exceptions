import os
def main():
    found = False
    cof_file = open('coffee222.txt', 'r')
    temp_file = open('tempfile.txt', 'w')
    search = input('Enter name of the searched coffee:')
    new_qty = float(input('Enter new quantity:'))
    descr = cof_file.readline()
    while descr != '':
        qty = cof_file.readline()
        descr = descr.rstrip('\n')
        qty = qty.strip('\n')
        if search == descr:
            found = True
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')
            print('Coffee', descr,'quantity was changed to:',new_qty)
        else:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        descr = cof_file.readline()
    cof_file.close()
    temp_file.close()
    os.remove('coffee222.txt')
    os.rename('tempfile.txt', 'coffee222.txt')
    if found:
        print('The name coffee was found in the file an qty was updated.')
    else:
        print('Searched coffe wasn\'t found in the file.')


main()
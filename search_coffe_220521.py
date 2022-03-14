def main():
    found = False
    file_cof = open('coffee22.txt', 'r')
    search = input('Enter name of coffee you are looking for:')
    descr = file_cof.readline()
    while descr != '':
        qty = file_cof.readline()
        descr = descr.rstrip('\n')
        qty = qty.rstrip('\n')
        if search == descr:
            found = True
            print('Description:', descr)
            print('Quantity:', qty)
        descr = file_cof.readline()
    if not found:
        print('Searched coffee was not found in the file.')

main()
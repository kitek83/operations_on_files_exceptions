def main():
    file = open('coffee22.txt', 'r')
    #all records must be read
    descr = file.readline()
    while descr != '':
        qty = file.readline()
        descr = descr.rstrip('\n')
        qty = qty.rstrip('\n')
        print('coffee descrip'
              'jtion:', descr)
        print('quantity',qty)
        descr = file.readline()
    file.close()
    print()
    print('Profram is finished.')

main()
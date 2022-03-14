def main():
    name_file = input('Enter name of file to be opened:')
    try:
        file = open(name_file, 'r')
        print(file.read())
    except IOError:
        print('There was an error trying \n'
              'to read the file named:',name_file)



main()
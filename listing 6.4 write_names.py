def main():
    print('Enter the names of the friends:')
    name1 = input('Friend #1:')
    name2 = input('Friend #2:')
    name3 = input('Friend #3:')
    #saving the names in the file
    file_names = open('names.txt','w')
    file_names.write(name1 + '\n')
    file_names.write(name2 + '\n')
    file_names.write(name3 + '\n')
    file_names.close()
    print('All names were saved in the file names.txt')
    print()
    print('----------------------------------------')
    print_names()
def print_names():
    print('Additionally all names will be printed in here.')
    file_names = open('names.txt', 'r')
    print(file_names.read())

main()
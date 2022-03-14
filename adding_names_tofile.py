#adding next 3 friends due to input func

def main():
    print('Adding next 3 friends due to function input.')
    name4 = input('Name #4:')
    name5 = input('Name #5:')
    name6= input('Name #6:')
    file = open('names.txt', 'a')
    file.write(name4 + '\n')
    file.write(name5 + '\n')
    file.write(name6 + '\n')
    file.write('Johny B\n')
    file.write('David G\n')
    file.write('Gorge.H\n')
    file.close()

    read_file()
def read_file():
    file = open('names.txt', 'r')
    print('Here you have all names saved to the file names.txt')
    print(file.read())



main()
def main():
    num1 = float(input('Enter nr1:'))
    num2 = float(input('Enter nr2:'))
    num3 = float(input('Enter nr3:'))
    file = open('numbers.txt', 'w')
    file.write(str(num1) + '\n')
    file.write(str(num2) + '\n')
    file.write(str(num3) + '\n')
    file.close()
    read_file()
def read_file():
    file = open('numbers.txt', 'r')
    print('You saved the following numbers in the file numbers.txt')
    print(file.read())


main()
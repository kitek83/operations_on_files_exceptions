def main():
    outfile = open('numbers.txt','w')
    number1 = int(input('Enter nr1:'))
    number2 = int(input('Enter nr2:'))
    number3 = int(input('Ente nr 3:'))
    #savinf numbers to the file
    outfile.write(str(number1) + '\n')
    outfile.write(str(number2) + '\n')
    outfile.write(str(number3) + '\n')
    outfile.close()
    print('Printing o'
          'ut saved numbers in the file numbers.txt')
    reading_outfile()
def reading_outfile():
    outfile = open('numbers.txt', 'r')
    print(outfile.read())

main()
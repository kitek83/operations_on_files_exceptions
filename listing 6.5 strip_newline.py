def main():
    file_read = open('philosophers.txt', 'r')
    #reding the lines from the file
    line1 = file_read.readline()
    line2 = file_read.readline()
    line3 = file_read.readline()
    #deleting the '\n' from the end of each line
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    print('Printing lines')
    print(line1)
    print(line2)
    print(line3)


main()
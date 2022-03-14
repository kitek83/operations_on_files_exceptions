#program, which is reading the lines from the file
def main():
    file = open('philosophers.txt', 'r')
    #reading lines from a file
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    file.close()
    print('Lines from the file philosophers.txt will be printed out.')
    print(line1)
    print(line2)
    print(line3)

main()

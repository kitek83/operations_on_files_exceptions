def main():
    infile = open('numbers.txt','r')
    num1 = float(infile.readline())
    num2 = float(infile.readline())
    num3 = float(infile.readline())
    infile.close()
    total = num1 + num2 + num3
    print('For the numbers',num1, num2, num3, 'total is:', total )
main()





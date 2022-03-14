def main():
    num_d = int(input('Enter how many days do you want to provide data:'))
    file = open('sales.txt', 'w')
    total = 0.0
    for count in range(1,num_d + 1):
        sales = float(input('Enter value of the sale on day nr:' + str(count) + ':'))
        total += sales
        file.write('The value of sales from the day:' + str(count) + 'is:')
        file.write(str(sales) + '\n')
        file.write('Total sale until day:' + str(count) + 'is:' + str(total) + '\n')
        file.write(str(print()))
    file.close()

    print('Values of sale for indicated days are saved in the file sales.txt')
    print('Data from the file sales will be printed out')
    read_file()
def read_file():
    file = open('sales.txt','r')
    print(file.read())

main()
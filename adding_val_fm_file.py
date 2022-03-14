def main():
    total = 0.0
    file = open('sales_data.txt','r')
    for val in file:
        total += float(val)

    print('Total sum of added values from the file is:',format(total,'.2f'))

main()
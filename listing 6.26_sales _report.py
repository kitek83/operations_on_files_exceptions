def main():
    total = 0.0
    try:
        file = open('sales_data.txt','r')
        for amount in file:
            total += float(amount)
        print('Total from file is:', total)
        file.close()
    except IOError:
        print('An error occured while reading a file.')
    except ValueError:
        print('There are other values than numerical in the file.')
    except:
        print('An error occured.')

main()
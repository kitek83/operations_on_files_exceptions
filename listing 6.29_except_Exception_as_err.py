def main():
    total = 0.0
    try:
        file = open('sales_data.txt', 'r')
        for z in file:
            total += float(z)

        file.close()

    except Exception as err:
        print('You made the following mistake:',err)
    finally:
        print('Total sum from the file is:', total)


main()
def main():
    file = open('sales2.txt', 'r')
    for line in file:
        amount = float(line)
        print(amount)
    file.close()


main()
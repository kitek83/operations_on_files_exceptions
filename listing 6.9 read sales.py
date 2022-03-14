def main():
    file = open('sales2.txt','r')
    lane = file.readline()
    while lane != '':
        amount = float(lane)
        print(amount)
        lane = file.readline()
    file.close()
main()
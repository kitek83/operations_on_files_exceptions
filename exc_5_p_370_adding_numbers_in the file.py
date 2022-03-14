def main():
    file = open('number_list.txt', 'r')
    print(file.read())
    print('Now all numbers will be added.')
    file = open('number_list.txt', 'r')
    total = 0.0
    c = 0
    for x in file:
        
        c += 1
        total += float(x)
        print('Until line nr',c,'total is:',total)
    average = total /c
    print('Total sum of all numbers in the file number_list.txt is:',total)
    print('Additionally average value for all numbers in the file is:', format(average,'.2f'))

main()
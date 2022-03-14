def main():
    num_file = open('number_list.txt', 'w')
    for x in range(1,101):
        print(x, end=',')
        num_file.write(str(x))
        num_file.write('\n')
    num_file.close()
    print('################################')
    print('Printing data from the file.')
    file = open('number_list.txt', 'r')
    print(file.read())
    



main()
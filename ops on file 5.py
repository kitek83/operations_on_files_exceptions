def main():
    file_ph = open('philosophers.txt','w')

    file_ph.write('John Lock \n')
    file_ph.write('David Hume \n')
    file_ph.write('Edmund Burke \n')
    file_ph.close()
    read()
def read():
    file_ph = open('philosophers.txt', 'r')
    print('Now the file is printing')
    print(file_ph.read())



main()
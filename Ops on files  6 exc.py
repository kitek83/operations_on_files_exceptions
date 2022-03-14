def main():
    file_t = open('today.txt','w')

    file_t.write('Today is beautiful day.\n')
    file_t.write('I am programming as susual.\n')
    file_t.write('I want to program all day')
    file_t.close()
    read()
def read():
    print('Now file today.txt will be printed out.')
    file_t = open('today.txt', 'r')
    print(file_t.read())

main()
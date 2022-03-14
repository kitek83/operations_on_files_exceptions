import os
def main():
    found = False
    file_s = open('student2.txt','a')
    temp_file = open('temp_file.txt', 'w')
    search = input('Enter the name you are looking for to change exam result.')
    descr = file_s.readline()
    while descr != '':
        res = file_s.readline()
        descr = descr.rstrip('\n')
        if search == descr:
            temp_file.write(descr + '\n')
            temp_file.write(str(100) + '\n')
        else:
            found = True
        descr = file_s.readline()
    file_s.close()
    temp_file.close()
    os.remove('students2.txt')
    os.rename('temp_file.txt', 'students2.txt')
    if found:
        print('File wasn\'t changed.')
    else:
        print('File was changed.')


main()
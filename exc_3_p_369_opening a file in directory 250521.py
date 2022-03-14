def main():
    import os
    entries = os.listdir() # opening current directory and assigning to var entries
    file_name = input('Enter file name with it\'s extension:')
    if file_name in entries:
        file = open(file_name, 'r')
        #print(file.read())
        count = 0
        for line in file:
            count += 1
            print(count,':',line)
    else:
        print('File wasn\'t found.')

    # print(entries)

main()
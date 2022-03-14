def main():
    file = open('number_list.txt','r')
    total = 0.0
    for x in file:
        total += float(x)
        print('Total for nr:',x,'is:', total)
        file2 = open('number_list2.txt','w')
        file2.write(str(total))
    print('Total sum added numbers from the file "number_list.txt" is:', total)
    file.close()

main()
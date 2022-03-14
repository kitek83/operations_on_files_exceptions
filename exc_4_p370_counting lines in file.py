def main():
    file = open('lines.txt','r')
    print('program will count nr of lines saved in file lines.txt')
    count = 0
    for line in file:
        count += 1
    print('There are', count,'lines in the file lines.txt')

main()
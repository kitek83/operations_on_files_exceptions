def main():
    file = open('lines.txt', 'r')
    for x in range(5):
        a = file.readline()
        print(a)

main()
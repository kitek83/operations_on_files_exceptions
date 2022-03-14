def main():
    file = open('my_name.txt', 'w')
    file.write('Krzysztof Kozak')
    file.close()
    print('Now file "my.name.txt" wil be read.')
    print()
    file2 = open('my_name.txt', 'r')
    print(file2.read())


main()
def main():
    file = open('number_list.txt', 'r')
    print(file.read())
    #print('###############################')
    print('I will change now string to float.')
    for x in file:
        print(float(x), end=', ')

main()
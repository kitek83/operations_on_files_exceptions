def main():
    em_file = open('employees.txt', 'r')
    for x in em_file:
        print(x)
    em_file.close()



main()
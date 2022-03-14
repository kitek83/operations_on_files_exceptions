def main():
    rec = int(input('Enter number of records to be created:'))
    em_file=open('employees.txt','w')
    for count in range(1, rec+1):
        print('Enter data for the worker nr:' + str(count)+'\n')
        name = input('Enter name of the worker:')
        id = float(input('Enter id of the worker:'))
        dep = input('Enter department of the worker:')
        em_file.write('-----------------------------------\n')
        em_file.write('This is the worker nr' + str(count)+':\n')
        em_file.write('Name:' + name + '\n')
        em_file.write('Id number:' + str(id) + '\n')
        em_file.write('Department:' + dep + '\n')
    em_file.close()
    print('All data was saved in file employees.')



main()
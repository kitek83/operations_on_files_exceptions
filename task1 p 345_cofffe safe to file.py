def main():
    file = open('coffee_record.txt', 'a')
    another = 't'
    while another == 't'or another == 'T':
        name_cof = input('Enter name of the coffee:')
        qty = float(input('Enter the quantity in kg of the coffee:'))
        file.write('--------------------------------------\n')
        file.write('name of coffee:' + name_cof + '\n')
        file.write('quantity of coffee:' + str(qty) + '\n')
        another = input('Enter t or T, if you want to put another record.')
    file.close()

main()
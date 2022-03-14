def main():
    another = 't'
    file_cof = open('coffee22.txt', 'a')
    while another == 't' or another == 'T':
        descr = input('Coffee description:')
        qty = float(input('Coffee quantity in kg:'))
        file_cof.write(descr + '\n')
        file_cof.write(str(qty) + '\n')
        another = input('Enter t or T to continue or another mark to close the program.')
    file_cof.close()
    print('Program is finished and data are saved to coffee22.txt file.')




main()
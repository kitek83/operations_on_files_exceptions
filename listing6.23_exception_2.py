def main():
    try:
        hours = int(input('Enter number of hours worked:'))
        pay_rate = float(input('Enter hourly pay rate:'))
        gross_pay = hours * pay_rate
        print('Gross pay is:', format(gross_pay, '.2f'))
    except ValueError:
        print('--------------------------------------------')
        print('Hours and pay rate must be numerical values.')
        print('--------------------------------------------')

main()
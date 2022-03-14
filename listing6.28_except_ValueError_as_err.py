def main():
    try:
        hours = int(input('Enter number of the overworked hours.'))
        pay_rate = int(input('Enter hourly pay rate.'))
        gross_pay = hours * pay_rate
        print('Your gross_pay is:',gross_pay)
    except ValueError as err:
        print(err)


main()
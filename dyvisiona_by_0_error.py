def main():
    try:
        num1 = float(input('Enter nr1:'))
        num2 = float(input('Enter nr2:'))
        result = num1 / num2
        print(num1, 'divided by', num2, 'is:',result)
    except ZeroDivisionError:
        print('You can\'t divide by 0')


main()
def main():
    num1 = int(input('Enter number1:'))
    num2 = int(input('Enter number 2:'))
    if num2 != 0:
        result = num1 / num2
        print(num1, 'divided by', num2, 'is:', format(result, '.2f'))
    else:
        print('You can\'t divide by 0!')


main()
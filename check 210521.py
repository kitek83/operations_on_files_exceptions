total = 0.0
for count in range(1,5+1):
    sale = float(input('Enter the data from the day nr' + str(count) + ':'))
    total += sale
    print('Total sum until today is:',total)
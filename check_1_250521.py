file = open('number_list.txt', 'r')
for x in file:
    print(float(x), end=', ')
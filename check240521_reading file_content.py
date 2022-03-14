file = open('sales_data.txt', 'r')
for x in file:
    print(float(x))

for x in range(10):
    print(x,end=',')
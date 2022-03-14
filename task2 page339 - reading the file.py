def main():
    file = open('frames.txt','r',)
    total = 0
    count = 0
    for line in file:
        amount = float(line)
        count += 1
        total += amount
        print('Time for the frame nr',count,'is:',amount)
    print('The duration of entire ad is:',total)


main()
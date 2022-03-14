def main():
    frame = int(input('Enter number of frames:'))
    file = open('frames.txt','w')
    for count in range(1, frame+1):
        time = int(input(str(count) + '.Enter the time in seconds for the current frame:'))
        file.write(str(time) + '\n')
    file.close()
    print('Data was saved in file frames.txt')


main()
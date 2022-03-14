def main():
    try:
        file = open(r'C:\Python Projects\python repetition1\HTML learning\media.html', 'r')
        print(file.read())
    except IOError as err:
        print(err)


main()
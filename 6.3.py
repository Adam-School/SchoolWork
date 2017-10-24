def main():
    with open("names.txt", "r") as ins:
        count = 0
        for line in ins:
            print(line)
            count += 1

    print('There are', count,' names in the text file')


main()

def main():

    path = 'CS202/Module3/CharCounter.py/sample3-1.txt'

    uppercaseAmount = 0
    lowercaseAmount = 0
    digitAmount = 0
    whitespaceAmount = 0

    try:
        with open(path, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    for char in contents:
        if char.isupper():
            uppercaseAmount += 1
        elif char.islower():
            lowercaseAmount += 1
        elif char.isdigit():
            digitAmount += 1
        elif char.isspace():
            whitespaceAmount += 1

    print("Amount of characters per type:")
    print("- uppercase letters:", uppercaseAmount)
    print("- owercase letters:", lowercaseAmount)
    print("- digits:", digitAmount)
    print("- whitespace characters:", whitespaceAmount)


if __name__ == "__main__":
    main()
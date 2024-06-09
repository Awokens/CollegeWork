def encryptFile(inputFile, codes):
    with open(inputFile, 'r') as file:
        content = file.read()
    decryptedContent = ''
    for char in content:
        if char in codes:
            decryptedContent += codes[char]
        else:
            decryptedContent += char
    file.close()
    print(decryptedContent)


def main():

    # dictionary
    codes = {
        '%': 'A',
        '9': 'a',
        '@': 'B',
        '#': 'b',
    }
    inputFile = 'CS202/Module4/Encrypted/encrypted_codes.txt'

    encryptFile(inputFile, codes)

if __name__ == "__main__":
    main()
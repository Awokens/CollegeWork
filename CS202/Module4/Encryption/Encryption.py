def encryptFile(inputFile, outputFile, codes):
    with open(inputFile, 'r') as file:
        content = file.read()
    file.close()
    encyptedContent = ''
    for char in content:
        if char in codes:
            encyptedContent += codes[char]
        else:
            encyptedContent += char

    with open(outputFile, 'w') as file:
        file.write(encyptedContent)
    file.close()

def main():

    # dictionary
    codes = {
        'A': '%',
        'a': '9',
        'B': '@',
        'b': '#',

    }

    inputFile = 'CS202/Module4/Decrypted/codes.txt'
    outputFile = 'CS202/Module4/Encrypted/encrypted_codes.txt'

    encryptFile(inputFile, outputFile, codes)

if __name__ == "__main__":
    main()
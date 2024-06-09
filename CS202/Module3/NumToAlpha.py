def letterToDigit(letter):
    letter = letter.upper()
    if 'A' <= letter <= 'C':
        return '2'
    elif 'D' <= letter <= 'F':
        return '3'
    elif 'G' <= letter <= 'I':
        return '4'
    elif 'J' <= letter <= 'L':
        return '5'
    elif 'M' <= letter <= 'O':
        return '6'
    elif 'P' <= letter <= 'S':
        return '7'
    elif 'T' <= letter <= 'V':
        return '8'
    elif 'W' <= letter <= 'Z':
        return '9'
    else:
        return letter

def translatePhoneNumber(phoneNum):
    phoneNum = phoneNum.upper()
    translatedNum = ""
    for char in phoneNum:
        translatedNum += letterToDigit(char)
    return translatedNum

def main():
    phoneNumInput = input("Enter a phone number (e.g. 509-GET-FOOD): ")
    translatedPhoneNum = translatePhoneNumber(phoneNumInput)
    print("Translated number:", translatedPhoneNum)

if __name__ == "__main__":
    main()

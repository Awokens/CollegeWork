def vowels(string):
    amount = 0
    for char in string:
        if char in "aeiouAEIOU":
            amount += 1
    return amount

def consonants(string):
    amount = 0
    for char in string:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            amount += 1
    return amount

if __name__ == "__main__":
    input = input("Enter a string: ")
    vowel_amount = vowels(input)
    consonant_amount = consonants(input)

    print("Number of vowels:", vowel_amount)
    print("Number of consonants:", consonant_amount)
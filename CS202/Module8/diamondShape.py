def diamondshape(n):

    # top half of the diamond shape
    for row in range(1, (n +1) // 2 + 1): 
        for space in range((n + 1)//2 - row):
            print(" ", end = "")
        for star in range((row * 2) - 1):
            print("*", end = "")
        print()

    # bottom half of the diamond shape
    for row in range((n + 1) // 2 + 1, n + 1): 
        for space in range(row - (n + 1)//2):
            print(" ", end = "")
        for star in range((n + 1 - row) * 2 - 1):
            print("*", end = "")
        print()

if __name__ == "__main__":
    n = int(input("How large do you want your diamond shape to be? "))
    diamondshape(n)

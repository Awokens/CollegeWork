import random

def main():
    # define variables even & odd
    even = 0
    odd = 0

    for i in range(0, 100): # iterate 100 times
        num = random.randint(1, 10) # generate rand num
        if num % 2 == 0: # calc if num is even or odd
            even += 1
        else:
            odd += 1
    # print results
    print(f'Odd numbers: {odd}')
    print(f'Even numbers: {even}')

# run main func
if __name__ == "__main__":
    main()
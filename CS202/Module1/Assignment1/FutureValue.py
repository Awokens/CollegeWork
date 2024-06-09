
def main():

    present_value = int(input('Enter the current value in the account: '))
    monthly_interest_rate = float(input('Enter the monthly interest rate: '))
    months = int(input('Enter the number of months that the money will be left in the account: '))

    result = getFutureValue(present_value, monthly_interest_rate, months)

    print(f'The future value of the account is: {result}')

def getFutureValue(present_value, monthly_interest_rate, months):
    future_value = present_value * (1 + (monthly_interest_rate))
    return f'{format(future_value, '.2f')}'

if __name__ == '__main__':
    main()
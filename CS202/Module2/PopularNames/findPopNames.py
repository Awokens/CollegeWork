
def checkPopularName(name, popNames, type):
    if name in popNames:
        print(f'{name} is a popular {type} name')
    else:
        print(f'{name} isn\'t the most popular {type} name')

def getNameInput(type):
    name = input(f'Enter a {type}\'s name (press Enter to skip): ').strip().capitalize()
    return name

def fetchNames(filename): 
    with open(filename, 'r') as file:
        names = [name.strip() for name in file]
    return names

def main():
    # initialize pop names girl/boy
    popBoyNames = fetchNames('CS202/Module2/PopularNames/BoyNames.txt')
    popGirlNames = fetchNames('CS202/Module2/PopularNames/GirlNames.txt')

    # get boy name input
    boyNameInput = getNameInput('boy')

    # get girl name input
    girlNameInput = getNameInput('girl')

    print('Popular name results of 2000 to 2009:')
    # if not skipped, check boy name input result
    if boyNameInput:
        checkPopularName(boyNameInput, popBoyNames, 'boy')
    # if not skipped, check girl name input result
    if girlNameInput:
        checkPopularName(girlNameInput, popGirlNames, 'girl')

if __name__ == '__main__':
    main()

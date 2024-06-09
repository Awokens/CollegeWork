import pickle

def main():

    contacts = cacheData()
    while True:
        print("\nMenu:")
        print("A. Look up gmail address")
        print("B. Add new user information")
        print("C. Update gmail address")
        print("D. Remove user data")
        print("E. Exit program")
        choice = input("Enter your number choice (1-5): ")
        if choice == 'A':
            fetchData(contacts)
        elif choice == 'B':
            createData(contacts)
        elif choice == 'C':
            updateData(contacts)
        elif choice == 'D':
            removeData(contacts)
        elif choice == 'E':
            saveData(contacts)
            print("Saving contacts data")
        else:
            print("Please try again.")


def updateData(contacts):
    name = input("Enter the name of contact: ")
    if name in contacts:
        gmail = input("Enter the new gmail address: ")
        contacts[name] = gmail
        print(f"Changed gmail address for {name} to {gmail}")
    else:
        print(f"No gmail address found for {name}")

def fetchData(contacts):
    name = input("Enter the name of contact: ")
    if name in contacts:
        gmail = contacts[name]
        print(f"\ngmail address for {name}: {gmail}")
    else:
        print(f"No gmail address found for {name}")

def createData(contacts):
    name = input("Enter the name of contact: ")
    gmail = input("Enter the gmail address: ")
    contacts[name] = gmail
    print(f"Added {name} with gmail address {gmail}")

def removeData(contacts):
    name = input("Enter the name of contact: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts")
    else:
        print(f"No gmail address found for {name}")

def cacheData():
    try:
        with open('CS202/Module4/Part2/contacts.pickle', 'rb') as file:
            contacts = pickle.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def saveData(contacts):
    with open('CS202/Module4/Part2/contacts.pickle', 'wb') as file:
        pickle.dump(contacts, file)

if __name__ == '__main__':
    main()
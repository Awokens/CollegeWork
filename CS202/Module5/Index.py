
import pet

def main(): 
    name = input('Enter name of pet: ') 
    animal_type = input('Enter your type of pet: ') 
    age = input("Enter your pet's age: ") 
    my_pet = pet.Pet(name, animal_type, age) 
    print(my_pet) 

if __name__ == "__main__":
    main()
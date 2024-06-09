class Pet: 
    def __init__(self, name, animal, age): 
        self.__name = name 
        self.__animal_type = animal 
        self.__age = age 
    def __str__(self): 
        return f"\nName: {self.__name}\nAnimal Type: {self.__animal_type}\nAge: {self.__age}\n"
    def set_name(self, name): 
        self.__name = name 
    def get_name(self): 
        return self.__name 
    def get_animal_type(self): 
        return self._animal__type 
    def set_age(self, age): 
        self.__age = age 
    def get_age(self): 
        return self.__age 
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type 
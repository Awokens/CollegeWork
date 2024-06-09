
class Person:

    def __init__(self, name, address, phoneNumber):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
    
    def __str__(self):
        return f'\nName: {self.name}\nAddress: {self.address}\nPhone Number: {self.phoneNumber}\n'
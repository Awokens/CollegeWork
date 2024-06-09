
from Person import Person
class Customer(Person):

    def __init__(self, name, address, phoneNumber, identifier, mailWishList: bool):
        super().__init__(name, address, phoneNumber)
        self.identifier = identifier
        self.mailWishList = mailWishList

    def __str__(self):    
        if self.mailWishList is True:
            isParticipant = 'Yes'
        else:
            isParticipant = 'No'
        return f'{super().__str__()}\nCustomer ID: {self.identifier}\nMail wishlist participant? {isParticipant}\n'




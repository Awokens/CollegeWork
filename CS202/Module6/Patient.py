class Patient:
    def __init__(self, firstName, middleName, lastName, address, city, state, postcode, phoneNumber, emergencyName, emergencyNumber):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.postcode = postcode
        self.phoneNumber = phoneNumber
        self.emergencyName = emergencyName
        self.emergencyNumber = emergencyNumber

    def getFirstName(self):
        return self.firstName
    def getMiddleName(self):
        return self.middleName
    def getLastName(self):
        return self.lastName
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def getState(self):
        return self.state
    def getPostcode(self):
        return self.postcode
    def getPhoneNumber(self):
        return self.phoneNumber
    def getEmergencyName(self):
        return self.emergencyName
    def getEmergencyNumber(self):
        return self.emergencyNumber
    def setFirstName(self, firstName):
        self.firstName = firstName
    def setMiddleName(self, middleName):
        self.middleName = middleName
    def setLastName(self, lastName):
        self.lastName = lastName
    def setAddress(self, address):
        self.address = address
    def setCity(self, city):
        self.city = city
    def setState(self, state):
        self.state = state
    def setPostcode(self, postcode):
        self.postcode = postcode
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    def setEmergencyName(self, emergencyName):
        self.emergencyName = emergencyName
    def setEmergencyNumber(self, emergencyNumber):
        self.emergencyNumber = emergencyNumber
    def __str__(self):
        return f'Patient: {self.firstName} {self.middleName} {self.lastName}\nAddress: {self.address} {self.city}, {self.state} {self.postcode}\nEmergency Contact Person: {self.emergencyName}\nEmergency Contact Number: {self.emergencyNumber}'
class Procedure:
    def __init__(self, procedureName, procedureDate, practitionerName, cost):
        self.procedureName = procedureName
        self.procedureDate = procedureDate
        self.practitionerName = practitionerName
        self.cost = cost

    def getProcedureName(self):
        return self.procedureName

    def setProcedureName(self, procedureName):
        self.procedureName = procedureName

    def getProcedureDate(self):
        return self.procedureDate

    def setProcedureDate(self, procedureDate):
        self.procedureDate = procedureDate

    def getPractitionerName(self):
        return self.practitionerName

    def setPractitionerName(self, practitionerName):
        self.practitionerName = practitionerName

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

    def __str__(self):
        return f'Procedure: {self.procedureName}\nDate: {self.procedureDate}\nPractitioner: {self.practitionerName}\nCost: {self.cost}'

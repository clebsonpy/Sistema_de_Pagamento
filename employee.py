import random
from insertData import InsertData

class Employee():

    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary
        self.codOnly = None
        self.paymentMethod = None
        self.belongUnion = None
        self.idUnion = None
        self.rateUnion = None
        self.paymentSchedule = None

    def paymentInfo(self, paymentMethod, belongUnion, idUnion, rateUnion, PaymentSchedule):
        insert = InsertData("Employees")
        insert.paymentInfo(self.codOnly, paymentMethod, belongUnion, idUnion, rateUnion, PaymentSchedule)

    def serviceRate(self, date, rate):
        insert = InsertData("Employees")
        insert.serviceRate(self.codOnly, date, rate

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Commission: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.commission, self.paymentMethod,
                                self.belongUnion, self.idUnion, self.rateUnion)

class Salared(Employee):

    def __init__(self, name, address, salary):
        super().__init__(name, address, salary)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Commission: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.commission, self.paymentMethod,
                                self.belongUnion, self.idUnion, self.rateUnion)

class Commissioner(Salared):

    def __init__(self, name, address, salary, commission):
        super().__init__(name, address, salary)
        self.commission = commission

    def salesHistory(self, date, value):
        insert = InsertData("Employees")
        insert.salesHistory(self.codOnly, date, value)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Commission: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.commission, self.paymentMethod,
                                self.belongUnion, self.idUnion, self.rateUnion)

class Hourly(Employee):

    def __init__(self, name, address, salary):
        super().__init__(name, address, salary)

    def timecard(self, date, hourly):
        insert = InsertData("Employees")
        if self.codOnly == None:
            return "Employee not exist!"
        else:
            insert.timecard(self.codOnly, date, hourly)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Commission: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.commission, self.paymentMethod,
                                self.belongUnion, self.idUnion, self.rateUnion)

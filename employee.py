import abc
from abc import abstractmethod
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

    def paymentInfo(self, paymentMethod, belongUnion, idUnion, rateUnion, PaymentSchedule = None):
        insert = InsertData("Employees")
        insert.paymentInfo(self.codOnly, paymentMethod, belongUnion, idUnion, rateUnion, PaymentSchedule)

    def serviceRate(self, date, rate):
        insert = InsertData("Employees")
        insert.serviceRate(self.codOnly, date, rate)

    @abstractmethod
    def payment(self):
        """Payment"""

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Commission: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}\n"\
               "paymentSchedule: {}>".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.commission, self.paymentMethod,
                                self.belongUnion, self.idUnion, self.rateUnion,
                                self.paymentSchedule)

class Salared(Employee):

    def __init__(self, name, address, salary):
        super().__init__(name, address, salary)
        self.description = "Salared"

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Salared: {}\n"\
               "Salary: {}\n"\
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}\n"\
               "paymentSchedule: {}>".format(self.codOnly, self.name,
                                self.address, self.salary, self.description,
                                self.paymentMethod, self.belongUnion,
                                self.idUnion, self.rateUnion, self.paymentSchedule)

class Commissioner(Salared):

    def __init__(self, name, address, salary, commission):
        super().__init__(name, address, salary)
        self.commission = commission
        self.description = "Commissioner"

    def salesHistory(self, date, value):
        insert = InsertData("Employees")
        insert.salesHistory(self.codOnly, date, value)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Commission: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}\n"\
               "paymentSchedule: {}>".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.commission,
                                self.paymentMethod, self.belongUnion,
                                self.idUnion, self.rateUnion, self.paymentSchedule)

class Hourly(Employee):

    def __init__(self, name, address, salary):
        super().__init__(name, address, salary)
        self.description = "Hourly"

    def timecard(self, date, hourly):
        insert = InsertData("Employees")
        if self.codOnly == None:
            return "Employee not exist!"
        else:
            insert.timecard(self.codOnly, date, hourly)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Code Only: {}\n" \
               "Name: {}\n" \
               "Address: {}\n" \
               "Description: {}\n" \
               "Salary: {}\n" \
               "Payment Method: {}\n" \
               "Belong Union: {}\n" \
               "Id Union: {}\n" \
               "Union Rate: {}\n"\
               "paymentSchedule: {}>".format(self.codOnly, self.name,
                                self.address, self.description,
                                self.salary, self.paymentMethod,
                                self.belongUnion, self.idUnion,
                                self.rateUnion, self.paymentSchedule)

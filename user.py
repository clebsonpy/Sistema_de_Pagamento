import random
from insertData import InsertData
from readData import ReadData
from removeData import RemoveData
from updateData import UpdateData

class AddEmployee():
    name_db = "Employees"

    def __init__(self, name, address, description, salary, commission):
        self.name = name
        self.address = address
        self.description = description
        self.salary = salary
        self.commission = commission
        self.codOnly = self.__setcodOnly()

    def __setcodOnly(self):
        objects = ReadData(self.name_db).readEmployee()
        ids = []
        for i in objects:
            ids.append(i.codOnly)

        idx = random.randint(1000, 10000)
        while idx in ids:
            idx = random.randint(100, 1000)
        return idx

    def save(self):
        insert = InsertData(self.name_db)
        insert.employee(self)


class RemoveEmployee():

    name_db = "Employees"

    def __init__(self, employeeCodOnly):
        self.employeeCodOnly = employeeCodOnly


    def remove(self):
        remove = RemoveData(self.name_db)
        remove.remove(self.employeeCodOnly)


class UpdateEmployee():

    name_db = "Employees"

    def __init__(self, objec, description = None):
        self.objec = objec
        self.description = description

    def update(self):
        update = UpdateData(self.name_db)
        update.updateEmployee(self.objec, self.description)
        update.updatePaymentInfo(self.objec)

from employee import Employee
from user import AddEmployee, RemoveEmployee, UpdateEmployee
from user import AddEmployee
from readData import ReadData

if __name__ == "__main__":

    #add = AddEmployee("Gabriel", "Rua da Floresta", "Commission", 2500, 0.05)
    #add.save()
    read = ReadData("Employees")
    employee = read.readEmployee(3158)
    print(employee)
    read.readPaymentMethod(employee)
    #print(read.readServiceRate(employee))
    #employee.serviceRate("2017/07/31", 100)
    #employee.paymentInfo("Depósito", "Sim", 3425, 0.05)
    print(employee)

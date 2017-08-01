from employee import Employee
from user import AddEmployee, RemoveEmployee, UpdateEmployee
from user import AddEmployee
from readData import ReadData
from systemPayment import SystemPayment
from interactionUser import InteractionUser

if __name__ == "__main__":

    name_db = "Employees"
    interaction = InteractionUser(name_db)
    interaction.menu()

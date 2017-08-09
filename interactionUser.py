from user import AddEmployee, UpdateEmployee, RemoveEmployee
from readData import ReadData

class InteractionUser():

    def __init__(self, name_db):
        self.name_db = name_db
        self.employee = None
        self.employees = None

    def employeeEnter(self):
        codOnly = int(input("Código Único: "))
        read = ReadData(self.name_db)
        self.employee = read.readEmployee(codOnly)
        self.menu()

    def menu(self):
        print("1 - Adição de um empregado\n"\
              "2 - Remoção de um empregado\n"\
              "3 - Lançar um Cartão de Ponto\n"\
              "4 - Lançar um Resultado Venda\n"\
              "5 - Lançar uma taxa de serviço\n"\
              "6 - Alterar detalhes de um empregado\n"\
              "7 - Rodar a folha de pagamento para hoje\n"\
              "8 - Undo/redo\n"\
              "9 - Agenda de Pagamento\n"\
              "0 - Criação de Novas Agendas de Pagamento\n"\
              "l - Empregado\n"\
              "a - Mostrar todos empregados\n"\
              "e - Sair")
        self.menuAction(input("Opção: "))

    def menuAction(self, op):
        if op == '1':
            self.addEmployee()
        elif op == '2':
            self.removeEmployee()
        elif op == '3':
            self.timecard()
        elif op == '4':
            self.salesHistory()
        elif op == '5':
            self.rateService()
        elif op == 'l':
            self.employeeEnter()
        elif op == '6':
            self.updateEmployee()
        elif op == 'a':
            self.eEmployees()

    def addEmployee(self):
        name = input("Nome: ")
        address = input("Endereço: ")
        description = input("Descrição: ")
        commission = float(input("Comissão: "))
        salary = float(input("Salário: "))
        employee = AddEmployee(name, address, description, salary, commission)
        employee.save()
        self.menu()

    def removeEmployee(self):
        if self.employee == None:
            print("Entre com o Empregado!")
            self.menu()
        remove = RemoveEmploye(self.employee.codOnly)
        remove.save()
        self.menu()

    def eEmployees(self):
        read = ReadData(self.name_db)
        self.employees = read.readEmployee()
        print(self.employees)
        self.menu()

    def rateService(self):
        date = input("Data: ")
        rate = float(input("Valor da Taxa: "))
        self.employee.serviceRate(date, rate)
        self.menu()

    def salesHistory(self):
        date = input("Data da Venda: ")
        value = float(input("Valor da Venda: "))
        self.employee.salesHistory(date, value)
        self.menu()

    def timecard(self):
        hour = float(input("Horas: "))
        date = input("Data: ")
        self.employee.timecard(date, hour)
        self.menu()

    def updateEmployee(self):
        description = None
        if self.employee == None:
            self.employeeEnter()
            self.updateEmployee()

        print("1 - Nome\n"\
              "2 - Endereço\n"\
              "3 - Descrição\n"\
              "4 - Método de Pagamento\n"\
              "5 - Pertence ao sindicato\n"\
              "6 - Taxa Sindical\n"\
              "7 - Código Sindicato\n"\
              "e - Sair")
        opu = input("Alterar: ")
        while opu != 'e':
            if opu == '1':
                self.employee.name = input("Nome: ")
            elif opu == '2':
                self.employee.address = input("Endereço: ")
            elif opu == '3':
                self.employee.description = input("Descrição: ")
            elif opu == '4':
                self.employee.paymentMethod = input("Método de Pagamento: ")
            elif opu == '5':
                self.employee.belongUnion = input("Pertence ao sindicato: ")
            elif opu == '6':
                self.employee.rateUnion = input("Taxa Sindical: ")
            elif opu == '7':
                self.employee.idUnion = input("Código Sindicato: ")
            opu = input("Alterar: ")

        update = UpdateEmployee(self.employee, description)
        update.save()
        self.menu()

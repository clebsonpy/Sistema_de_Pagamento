from user import AddEmployee, UpdateEmployee, RemoveEmployee
from readData import ReadData

class InteractionUser():

    def __init__(self, name_db):
        self.name_db = name_db

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
              "exit - Sair")
        self.menuAction(input("Opção: "))

    def menuAction(self, op):
        if op == '1':
            self.addEmployee()
        elif op == '2':
            self.removeEmployee()
        elif op == '6':
            self.updateEmployee()


    def addEmployee(self):
        name = input("Nome: ")
        address = input("Endereço: ")
        description = input("Descrição: ")
        commission = float(input("Comissão: "))
        salary = float(input("Salário: "))
        employee = AddEmployee(name, address, description, salary, commission)
        employee.save()
        self.menu()

    def removeEmployee(self, op):
        codOnly = int(input("Código Único: "))
        remove = RemoveEmploye(codOnly)
        remove.save()
        self.menu()

    def updateEmployee(self):
        codOnly = int(input("Código Único: "))
        read = ReadData(self.name_db)
        employee = read.readEmployee(codOnly)
        description = None
        print("1 - Nome\n"\
              "2 - Endereço\n"\
              "3 - Descrição\n"\
              "4 - Método de Pagamento\n"\
              "5 - Pertence ao sindicato\n"\
              "6 - Taxa Sindical\n"\
              "exit - Sair")
        opu = input("Alterar: ")
        while opu != 'exit':
            if opu == '1':
                employee.name = input("Nome: ")
            elif opu == '2':
                employee.address = input("Endereço: ")
            elif opu == '3':
                employee.description = input("Descrição: ")
            elif opu == '4':
                employee.paymentMethod = input("Método de Pagamento: ")
            elif opu == '5':
                employee.belongUnion = input("Pertence ao sindicato")
            elif opu == '6':
                employee.rateUnion = input("Taxa Sindical: ")
            opu = input("Alterar: ")

        update = UpdateEmployee(employee, description)
        update.save()
        self.menu()

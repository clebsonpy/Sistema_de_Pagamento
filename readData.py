import connecting as conn
from employee import Employee, Commissioner, Hourly, Salared

class ReadData():

    def __init__(self, name_db):
        self.name_db = name_db

    def readEmployee(self, employeeCodOnly=None):
        db = conn.Connect(self.name_db)
        if employeeCodOnly == None:
            sql = "SELECT * FROM Employee"
            db.cursor.execute(sql)
            list = db.cursor.fetchall()
            employees = []
            for data in list:
                employee = self.__employee(data)
                employee = self.readPaymentInfo(employee)
                employees.append(employee)
            db.close_db()
            return employees
        else:
            sql = "SELECT * FROM Employee WHERE codOnly = %s" % employeeCodOnly
            db.cursor.execute(sql)
            data = db.cursor.fetchone()
            employee = self.__employee(data)
            db.close_db()
            return employee

    def __employee(self, data):
        codOnly, name, address, description, salary, commission = data
        if description == "Hourly":
            employee = Hourly(name, address, salary)
            employee.codOnly = codOnly
            return employee

        elif description == "Salared":
            employee = Salared(name, address, salary)
            employee.codOnly = codOnly
            return employee

        elif description == "Commissioner":
            employee = Commissioner(name, address, salary, commission)
            employee.codOnly = codOnly
            return employee

    def readPaymentInfo(self, objec):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM PaymentInfo WHERE codOnly = %s" % objec.codOnly
        db.cursor.execute(sql)
        paymentInfo = db.cursor.fetchone()
        db.close_db()
        if paymentInfo == None:
            return objec
        else:
            codOnly, paymentMethod, belongUnion, idUnion, rateUnion, paymentSchedule = paymentInfo
            objec.paymentMethod = paymentMethod
            objec.belongUnion = belongUnion
            objec.idUnion = idUnion
            objec.rateUnion = rateUnion
            objec.paymentSchedule = paymentSchedule
            return objec

    def readTimecard(self, objectHourly):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM Timecard WHERE codOnly = %s" % objectHourly.codOnly
        db.cursor.execute(sql)
        timecard = db.cursor.fetchall()
        db.close_db()
        return timecard

    def readSalesHistory(self, objectCommissioner, previousPayment):
        db = conn.Connect(self.name_db)
        if previousPayment == None:
            sql = "SELECT * FROM SalesHistory WHERE codOnly = %s" \
                %(objectCommissioner.codOnly)
        else:
            sql = "SELECT * FROM SalesHistory WHERE codOnly = %s AND date > %s" \
                %(objectCommissioner.codOnly, previousPayment)

        db.cursor.execute(sql)
        salesHistory = db.cursor.fetchall()
        db.close_db()
        return salesHistory

    def readServiceRate(self, objec, previousPayment):
        db = conn.Connect(self.name_db)
        if previousPayment == None:
            sql = "SELECT * FROM ServiceRate WHERE codOnly = %s" \
                %(objec.codOnly)
        else:
            sql = "SELECT * FROM ServiceRate WHERE codOnly = %s AND date > %s" \
                %(objec.codOnly, previousPayment)

        db.cursor.execute(sql)
        serviceRate = db.cursor.fetchall()
        db.close_db()
        return serviceRate

    def readPaymentHistory(self, objec):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM PaymentHistory WHERE codOnly = %s" % objec.codOnly
        db.cursor.execute(sql)
        paymentHistory = db.cursor.fetchall()
        if paymentHistory == []:
            previousPayment = None
        else:
            previousPayment = paymentHistory[-1]
        db.close_db()
        return paymentHistory, previousPayment

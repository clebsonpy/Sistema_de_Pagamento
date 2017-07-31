import connecting as conn
from employee import Employee

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
            for i in list:
                codOnly, name, address, description, salary, commission = i
                employee = Employee(name, address, description, salary, commission)
                employee.codOnly = codOnly
                employees.append(employee)
            db.close_db()
            return employees
        else:
            sql = "SELECT * FROM Employee WHERE codOnly = %s" % employeeCodOnly
            db.cursor.execute(sql)
            employee = db.cursor.fetchone()
            codOnly, name, address, description, salary, commission = employee
            employee = Employee(name, address, description, salary, commission)
            employee.codOnly = codOnly
            db.close_db()
            return employee

    def readPaymentMethod(self, objec):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM PaymentInfo WHERE codOnly = %s" % objec.codOnly
        db.cursor.execute(sql)
        paymentInfo = db.cursor.fetchone()
        codOnly, paymentMethod, belongUnion, idUnion, rateUnion = paymentInfo
        objec.paymentMethod = paymentMethod
        objec.belongUnion = belongUnion
        objec.idUnion = idUnion
        objec.rateUnion = rateUnion
        db.close_db()

    def readTimecard(self, objec):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM Timecard WHERE codOnly = %s" % objec.codOnly
        db.cursor.execute(sql)
        timecard = db.cursor.fetchall()
        db.close_db()
        return timecard

    def readSalesHistory(self, objec, previousPayment):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM SalesHistory WHERE codOnly = %s AND date > %s" \
            %(objec.codOnly, previousPayment)
        db.cursor.execute(sql)
        salesHistory = db.cursor.fetchall()
        db.close_db()
        return salesHistory

    def readServiceRate(self, objec, previousPayment):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM ServiceRate WHERE codOnly = %s AND date > %s" \
            %(objec.codOnly, previousPayment)
        db.cursor.execute(sql)
        serviceRate = db.cursor.fetchall()
        db.close_db()
        return serviceRate

    def readPaymentHistory(self, object):
        db = conn.Connect(self.name_db)
        sql = "SELECT * FROM PaymentHistory WHERE codOnly = %s" % objec.codOnly
        db.cursor.execute(sql)
        paymentHistory = db.cursor.fetchall()
        previousPayment = paymentHistory[-1]
        db.close_db()
        return paymentHistory, previousPayment

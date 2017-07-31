import connecting as conn

class RemoveData():

    def __init__(self, employeeCodOnly):
        self.employeeCodOnly = employeeCodOnly
        self.name_db = "Employees"

    def removeEmployee(self):
        db = conn.Connect(self.name_db)
        sql = """DELETE FROM Employee WHERE codOnly = %s""" % self.employeeCodOnly
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()
        self.removePaymentInfo()
        self.removeSalesHistory()
        self.removeTimecard()
        self.removeServiceRate()

    def removePaymentInfo(self):
        db = conn.Connect(self.name_db)
        sql = """DELETE FROM PaymentInfo WHERE codOnly = %s""" % self.employeeCodOnly
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def removeTimecard(self):
        db = conn.Connect(self.name_db)
        sql = """DELETE FROM Timecard WHERE codOnly = %s""" % self.employeeCodOnly
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def removeSalesHistory(self):
        db = conn.Connect(self.name_db)
        sql = """DELETE FROM SalesHistory WHERE codOnly = %s""" % self.employeeCodOnly
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def removeServiceRate(self):
        db = conn.Connect(self.name_db)
        sql = """DELETE FROM ServiceRate WHERE codOnly = %s""" % self.employeeCodOnly
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()
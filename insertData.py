import connecting as conn

class InsertData():

    def __init__(self, name_db):
        self.name_db = name_db


    def employee(self, objec):
        codOnly = objec.codOnly
        firstName = objec.name
        address = objec.address
        description = objec.description
        salary = objec.salary
        commission = objec.commission
        db = conn.Connect(self.name_db)
        sql = """INSERT INTO Employee(codOnly, firstName, address, description, salary, commission) VALUES(%s, '%s', '%s', '%s', %s, %s)"""\
                % (codOnly, firstName, address, description, salary, commission)

        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def timecard(self, codOnly, date, hourly):
        db = conn.Connect(self.name_db)
        sql = """INSERT INTO Timecard(codOnly, date, hourly) VALUES (%s, '%s', %s)""" \
              % (codOnly, date, hourly)

        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def salesHistory(self, codOnly, date, value):
        db = conn.Connect(self.name_db)
        sql = """INSERT INTO SalesHistory(codOnly, date, value) VALUES (%s, '%s', %s)""" \
              %(codOnly, date, value)
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def paymentInfo(self, codOnly, paymentMethod, belongUnion, idUnion, rateUnion, paymentSchedule):
        db = conn.Connect(self.name_db)
        if paymentSchedule == None:
            sql = sql = """INSERT INTO PaymentInfo(codOnly, paymentMethod, belongUnion, idUnion, rateUnion) VALUES (%s, '%s', '%s', %s, %s)""" \
                  %(codOnly, paymentMethod, belongUnion, idUnion, rateUnion)
        else:
            sql = """INSERT INTO PaymentInfo(codOnly, paymentMethod, belongUnion, idUnion, rateUnion, paymentSchedule) VALUES (%s, '%s', '%s', %s, %s, '%s')""" \
                  %(codOnly, paymentMethod, belongUnion, idUnion, rateUnion, paymentSchedule)

        
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def serviceRate(self, codOnly, date, rate):
        db = conn.Connect(self.name_db)
        sql = """INSERT INTO ServiceRate(codOnly, date, rate) VALUES (%s, '%s', %s)""" \
              %(codOnly, date, rate)
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def paymentHistory(self, codOnly, datePayment, value):
        db = conn.Connect(self.name_db)
        sql = """INSERT INTO PaymentHistory(codOnly, previousPayment, value) VALUES (%s, '%s', %s)""" \
              %(codOnly, datePayment, value)
        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

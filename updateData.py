import connecting as conn
from readData import ReadData

class UpdateData():

    def __init__(self, name_db):
        self.name_db = name_db

    def updateEmployee(self, objec):
        codOnly = objec.codOnly
        firstName = objec.name
        address = objec.address
        description = objec.description
        db = conn.Connect(self.name_db)
        sql = """UPDATE Employee SET firstName = '%s', address = '%s', description = '%s' WHERE codOnly = %s"""\
              % (firstName, address, description, codOnly)

        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()

    def updatePaymentInfo(self, objec):
        codOnly = objec.codOnly
        paymentMethod = objec.paymentMethod
        belongUnion = objec.belongUnion
        idUnion = objec.idUnion
        rateUnion = objec.rateUnion
        db = conn.Connect(self.name_db)
        sql = """UPDATE Employee SET paymentMethod = '%s', belongUnion = '%s', idUnion = %s, rateUnion = %s WHERE codOnly = %s""" \
              % (paymentMethod, belongUnion, idUnion, rateUnion, codOnly)

        db.cursor.execute(sql)
        db.commit_db()
        db.close_db()
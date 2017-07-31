from readData import ReadData
from insertData import InsertData

class SystemPayment():

    name_db = "Employees"

    def __init__(self, objec, date, rateDiscounts):
        self.objec = objec
        self.date = date
        self.rateDiscounts = rateDiscounts

    def paymentCommission(self):
        read = ReadData(self.name_db)
        previousPayment = read.readPaymentHistory(self.objec)[1]
        salesHistory = read.readSalesHistory(self.objec, previousPayment)
        serviceRate = read.readServiceRate(self.objec, previousPayment)
        totalRate = 0
        for rate in serviceRate:
            totalRate += rate[2]
        totalSales = 0
        for sales in salesHistory:
            totalSales += sales[2]

        payment = object.salary + (totalSales * object.commission)
        paymentLiquid = self.discounts(payment, totalRate)
        insert = InsertData(self.name_db)
        insert.paymentHistory(object.codOnly, self.date, payment)
        return paymentLiquid, payment

    def paymentSalary(self):
        totalRate = 0
        for rate in serviceRate:
            totalRate += rate[2]
        totalSales = 0
        paymentLiquid = self.discounts(payment, totalRate)
        insert = InsertData(self.name_db)
        insert.paymentHistory(object.codOnly, self.date, payment)
        return paymentLiquid, payment

    def paymentHourly(self):



    def discounts(self, payment, totalRate):
        paymentLiquid = ((100 - self.rateDiscounts)/100) * payment
        return paymentLiquid - totalRate

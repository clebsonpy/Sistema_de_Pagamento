import sqlite3

#Criando e Conectando-se com o nome_db
conn = sqlite3.connect('Employees.db')
#Cursor do nome_db
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Employee(
codOnly INTEGER PRIMARY KEY,
firstName VARCHAR(50) NOT NULL,
address VARCHAR(100) NOT NULL,
description VARCHAR(25) NOT NULL,
salary FLOAT NOT NULL,
commission FLOAT NULL)""")

cursor.execute("""CREATE TABLE PaymentInfo(
codOnly INTEGER NOT NULL,
paymentMethod VARCHAR(25) NOT NULL,
belongUnion VARCHAR(3) NOT NULL,
idUnion INTEGER,
rateUnion FLOAT,
PaymentSchedule VARCHAR(25),
FOREIGN KEY(codOnly) REFERENCES Employee(codOnly)
)""")

cursor.execute("""CREATE TABLE Timecard(
codOnly INTEGER NOT NULL,
date DATETIME NOT NULL,
hourly FLOAT NOT NULL,
FOREIGN KEY(codOnly) REFERENCES Employee(codOnly)
)""")

cursor.execute("""CREATE TABLE SalesHistory(
codOnly INTEGER NOT NULL,
date DATETIME NOT NULL,
value FLOAT NOT NULL,
FOREIGN KEY(codOnly) REFERENCES Employee(codOnly)
)""")

cursor.execute("""CREATE TABLE ServiceRate(
codOnly INTEGER NOT NULL,
date DATETIME NOT NULL,
rate FLOAT NOT NULL,
FOREIGN KEY(codOnly) REFERENCES Employee(codOnly)
)""")

cursor.execute("""CREATE TABLE PaymentHistory(
codOnly INTEGER NOT NULL,
previousPayment DATETIME NOT NULL,
valueGross FLOAT NOT NULL,
valueLiquid FLOAT NOT NULL,
FOREIGN KEY(codOnly) REFERENCES Employee(codOnly)
)""")

print('Banco criando com sucesso!')
#Fechando Conexão
cursor.close()

import mysql.connector

mydb = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n",
    database="sql11404167"
)

mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customer1_MRO" # !!!!!!!! VORSICHT - LÖSCHT EXISTIERENDE DATENBANK
mycursor.execute(sql)
mycursor.execute("CREATE TABLE customer1_MRO (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for tables in mycursor:
   print(tables)

mycursor.execute("ALTER TABLE customer1_MRO ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO customer1_MRO (name, address) VALUES (%s, %s)"
#values = ("Michael", "Straße 530")
#mycursor.execute(sql, values)
values = [("abc", "Straße 1"), ("xyz", "Straße 2"), ("Klk", "Straße 1")]
mycursor.executemany(sql,values)

mydb.commit()

print(mycursor.rowcount, "... Anzahl an Datensätzen")
print("ID: ", mycursor.lastrowid)

sql = "SELECT * FROM customer1_MRO WHERE address = 'Straße 1'"
mycursor.execute(sql)
#myresult = mycursor.fetchone()
#print(myresult)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)

mydb.close()
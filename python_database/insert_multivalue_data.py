try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306",database="School")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql='INSERT INTO Student(Srno,Name,Age)values(1,"Ram Das",12),(2,"Laxman Dey",34),(3,"Sita Dutta",56)'
myc=conn.cursor()
try:
    myc.executemany(sql)
    print("Data Inserted Succesfully")
    conn.commit()                   # this comit function is uses to insert multiple data in databases
except:
    print("Unable to Insert Data")
    myc.close()
conn.close()

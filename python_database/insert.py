try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306",database="School")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql='INSERT INTO Student(Srno,Name,Age)values(1,"Ram Das",12)'
myc=conn.cursor()
try:
    myc.execute(sql)
    print("Data Inserted Succesfully")
    conn.commit()
except:
    print("Unable to Insert Data")
    myc.close()
conn.close()

try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306",database="School")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql="CREATE TABLE Student(Sno int(10),Name varchar(200),Age int(10))"
myc=conn.cursor()
try:
    myc.execute(sql)
    print("Table Created Succesfully")
except:
    print("Unable to Create Table")
    myc.close()
conn.close()
try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql="CREATE DATABASE School"
myc=conn.cursor()
try:
    myc.execute(sql)
    print("Database Created Succesfully")
except:
    print("Unable to Create Database")
    myc.close()
conn.close()
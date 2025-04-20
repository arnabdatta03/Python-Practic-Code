try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306",database="School")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql="DELETE FROM student WHERE Srno=2"
myc=conn.cursor()
try:
    myc.execute(sql)
    print("Data Deleted Succesfully")
    conn.commit()
except:
    print("Unable to Delete Data")
    myc.rollback()
    myc.close()
conn.close()

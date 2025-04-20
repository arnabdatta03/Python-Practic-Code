try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306",database="School")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql="UPDATE STUDENT SET Name='Laxman Dey',Address='Kolkata',Age=35 WHERE Srno=3"
myc=conn.cursor()
try:
    myc.execute(sql)
    print("Data Updated Succesfully")
    conn.commit()
except:
    print("Unable to Update Data")
    myc.rollback()
    myc.close()
conn.close()
try:
    import mysql.connector #library
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306",database="School")
    if(conn.is_connected()):
        print("Connected")
except:
    print("Not Connected")

sql="SELECT *FR0M student"
myc=conn.cursor()
try:
    myc.execute(sql)
    row=myc.fetchone()
    while row is not None:
        Srno=row[0]
        Name=row[1]
        Email=row[2]
        Phn=row[3]
        print(Srno,Name,Email,Phn)
        row=myc.fetchone()
except:
    print("Unable to Update Data")
    myc.rollback()
    myc.close()
conn.close()
try:
    import mysql.connector
    conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3307",database="School")
    if conn.is_connected():
        print("Connected")
except:
    print("Not Connected")

Srno=int(input("Enter the Serial No:"))
Name=input("Enter the Name:")
Address=input("Enter the Address:")

val=(Srno,Name,Address)

sql='INSERT INTO Student(Srno,Name,Address)values(%s,%s,%s)'
myc=conn.cursor()
try:
    myc.execute(sql,val)
    print("Data Inserted Succesfully")
    conn.commit()
except:
    print("Unable to Insert Data")
conn.close()

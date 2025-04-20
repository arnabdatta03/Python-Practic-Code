import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="12345",port="3306")
if(conn.is_connected()):
    print("Connection Success")
else:
    print("Connection failed")
conn.close()
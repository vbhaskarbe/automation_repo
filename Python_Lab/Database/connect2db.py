import mysql.connector
from mysql.connector import Error


try:
    #connection = mysql.connector.connect(host='localhost', database="SANKALP_DB",user='root', password='bad_welcome123')
    #connection = mysql.connector.connect(host='localhost', database="SANKALP_DB",user='root', password='bad_welcome123', auth_plugin='mysql_native_password')
    #connection = mysql.connector.connect(host='localhost', database="SANKALP_DB",user='bad_root', password='welcome123', auth_plugin='mysql_native_password')
    #connection = mysql.connector.connect(host='localhost', database="SANKALP_DB_BAD",user='root', password='welcome123', auth_plugin='mysql_native_password')
    #connection = mysql.connector.connect(host='localhost_bad', database="SANKALP_DB",user='root', password='welcome123', auth_plugin='mysql_native_password')
    connection = mysql.connector.connect(host='localhost', database="SANKALPDB",user='root', password='welcome123', auth_plugin='mysql_native_password')
    print(connection)

    if connection.is_connected() :
        print("Connection to DB is establoshed")
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You are connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
   print("Winding up")
   if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



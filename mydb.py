import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='fhel123',
    auth_plugin='mysql_native_password'  # This should now work!
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("Database created successfully!")

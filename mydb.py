 
import mysql.connector

# Establish the connection
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Masud5049"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Execute the CREATE DATABASE command
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")

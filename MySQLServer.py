# Import modules
import mysql.connector
from mysql.connector import connect, Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "stennis",
        password = "Password123!",
        )
        
    mycursor = mydb.cursor()
    
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alxbookstore')
    print("Database 'alxbookstore' created or alredy exists!")
    
    # close the conncetion 
    mycursor.close()
    mydb.close()
    
    with connect(
            host = "localhost",
            user = "stennis",
            password = "Password123!",
            database = "alxbookstore",
            ) as connection:
                print(connection)

except Error as e:
    print("Error: ", e)
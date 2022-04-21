#please check and subscribe my channel(https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos)
#https://www.github.com/wintun-devop
from pymysql import *

#create database connection to database server on localhost,username and password I have used here is sample illustrations.
db_connection=connect(
    host="localhost",
    user = "alldbuser",
    passwd="Xyz123!@#"
)
#This curser is associated to whole database
db_curser=db_connection.cursor()

def list_all_databases():
    db_curser.execute("SHOW DATABASES")
    print("All databases are here.")
    for databases in db_curser:
        print(databases)

#create database table on a specific databases
def create_database_table():
    specific_db_connection=connect(
        host="localhost",
        user = "alldbuser",
        passwd="Xyz123!@#",
        database="testdb01"
        )
    specific_curser=specific_db_connection.cursor()
    try:
        specific_curser.execute("CREATE TABLE users (id INTEGER AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(100) NOT NULL,lastname VARCHAR(100),email VARCHAR(150) NOT NULL,DOB DATE,contact VARCHAR(20))")
        print("Database table has been created successfully!")
    except:
        print("Database table already exist.")
    
    


def main():
    create_database_table()

if __name__=="__main__":
    main()

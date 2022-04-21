#please check and subscribe my channel(https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos)
#https://www.github.com/wintun-devop

from pymysql import *
#create database connection to database server on localhost,username and password I have used here is sample illustrations.
db_connection=connect(
    host="localhost",
    user = "alldbuser",
    passwd="Xyz123!@#"
)
#database connection testing
def connection_object():
    print("Database was connected successfully on",db_connection,".")

#define database execution curser,we will use this curser to perform database operation
db_cursor=db_connection.cursor()

#create a database by function,with error control
def create_db():
    db_cursor.execute("SHOW DATABASES")
    print("All database on system.")
    for db_list in db_cursor:
        print(db_list)
    db_name=str(input("Enter your database name:"))
    try:
        db_cursor.execute("CREATE DATABASE {}".format(db_name))
        print("Database have been created successfully.")
    except:
        print("Can not create database {} as it is already exists.".format(db_name))
#list all the databases by function
def check_db_list():
    db_cursor.execute("SHOW DATABASES")
    print("All database list in the system.")
    for db_list in db_cursor:
        print(db_list)
#drop a database by function with error control
def drop_db():
    db_cursor.execute("SHOW DATABASES")
    print("All database on system.")
    for db_list in db_cursor:
        print(db_list)
    print("Which one you would like to drop? Please be careful to drop!")
    drop_db_name=str(input("Enter your database to drop:"))
    try:
        db_cursor.execute("DROP DATABASE {}".format(drop_db_name))
        print("{} was drop successfully!".format(drop_db_name))
    except:
        print("The input you enter {} is not in databases.!".format(drop_db_name))




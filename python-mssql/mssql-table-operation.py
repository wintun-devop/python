#pip install pypyodbc pyodbc pymssql
#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos

import pypyodbc as odbc

DRIVER_NAME ="SQL Server"
#please server host name here correctly,otherwise,it won't work out.
SERVER_NAME ="SERVER-HOST-NAME"
DATABASE_NAME ="test_db_03"

#uid = username
#password = password

#Define contents for database instance for connections
connection_string= f"""
   DRIVER={{{DRIVER_NAME}}};
   SERVER={SERVER_NAME};
   DATABASE={DATABASE_NAME};
   Trust_Connection=yes;
"""
#define database connection
db_connection=odbc.connect(connection_string)
#define database conection for dbconnection cursor
db_cursor=db_connection.cursor()

def create_table():
    db_cursor.execute("""
                      CREATE TABLE students(
                         id INT IDENTITY(1,1) PRIMARY KEY,
                         firstname nvarchar(100),
                         lastname nvarchar(100),
                         email nvarchar(200),
                         dob date 
                      )
                      """)
    db_connection.commit()
    print(f"Database table created successfully!")
    
def insert_data():
   db_cursor.execute("""
                     INSERT INTO students (firstname,lastname,email,dob)
                     VALUES
                        ('Win Tun','Hlaing','wintun.edu@gmail.com','1987-10-30'),
                        ('La Pyae','Wunn','lapyaewunn@gmail.com','1990-10-30'),
                        ('Sein','Lei','seinlei@gmail.com','2000-10-30'),
                        ('Layaun','Linn','layaunglinn@gmail.com','2000-11-30')
                     """)
   db_connection.commit()
   print(f"Data insert into database table successfully!")
   
def main():
   insert_data()
   
if __name__ == "__main__":
   main() 
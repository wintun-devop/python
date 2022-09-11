

import psycopg2
from psycopg2 import connect, extensions, sql
#establishing the connection
"""
postgres_connection = psycopg2.connect(
   database="postgres", user='iamadmin',
   password='BarNarTharDaKar',
   host='172.18.0.2',
   port= '5432'
)
"""
def database_establish(db_name,db_user,db_password,db_host):
    db_connection = psycopg2.connect(
    database=db_name, user=db_user,
    password=db_password,
    host=db_host,
    port= '5432'
    )
    db_cursor=db_connection.cursor()
    return db_cursor

def check_tabledata_list(table_name):
    db_connection_cursor=database_establish("dvd_rental_01","dbadmin","Abc123Abc123","172.18.0.3")
    db_connection_cursor.execute("SELECT * FROM {};".format(table_name))
    db_rows=db_connection_cursor.fetchall()
    db_row_number=db_connection_cursor.rowcount
    for row in db_rows:
        print(row)
    print(db_row_number)
    db_connection_cursor.close()

def create_database(databae_name):
    database=databae_name
    db_connection=connect(dbname="dvd_rental_01",user="dbadmin",host="172.18.0.3",password="Abc123Abc123")
    """
    ISOLATION LEVELS for psycopg2,0 = READ UNCOMMITTED,1 = READ COMMITTED,2 = REPEATABLE READ,3 = SERIALIZABLE,4 = DEFAULT
    """
    #get the isolation leve for autocommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    db_connection.set_isolation_level(autocommit)
    # set the isolation level for the connection's cursors
    db_connection_cursor=db_connection.cursor()
    #error control for database already exit
    try:
        # use the sql module instead to avoid SQL injection attacks
        db_connection_cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))
        #close the cursor and connection to avoid memory leaks
        db_connection.close()
        db_connection_cursor.close()
        print(f"The database {database} has been created successfully.")
    except:
        print(f"The database named {database} already exist.")

def main():
    create_database("test_db_02")
    
if __name__=="__main__":
    main()

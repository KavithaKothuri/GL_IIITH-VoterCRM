# pip install mysql-connector-python streamlit
# pip install mysql-connector-python
import pandas as pd
from Insert_data import *
from sqlconnection import *

# Establish a database connection
def create_server_connection(connection):
    # Implement the logic to create the server connection
    if connection is not None:
        connection = create_server_connection()
        try:
            cursor = connection.cursor()
            print(" My SQL database connection successful")
        except Exception as err:
            print(f"Failed to establish a database connection")       
    return connection

def create_and_switch_database(connection, database, switch_db):
    cursor = connection.cursor()
    try:
        drop_query = "DROP DATABASE IF EXISTS " + database
        db_query = " CREATE DATABASE " + database
        switch_query = " USE " + switch_db
        cursor.execute(drop_query)
        cursor.execute(db_query)
        cursor.execute(switch_query)
        print(" Database created successfully")
    except Exception as err:
        print("Error in creating database: '{err}'")

def create_table(connection, table_creation_statement):
    cursor = connection.cursor()
    try:
        cursor.execute(table_creation_statement)
        connection.commit()
        print("Table creation successful")
    except Exception as err:
        print("Error in table creation: '{err}'")

def close_connection(connection):
    if connection:
        connection.close()

if __name__ == "__main__":
    connection = create_server_connection()
    create_and_switch_database(connection, database, database)
    create_table(connection, create_voter_table) 
    close_connection(connection)

import csv
from sqlconnection import connection
import database as db

DB = "VOTER_DATA"  # This is the name of the database 

CONFIG_PATH = "D:\CAPSTONE PROJECT\voterCRM\voterCRM sample data.xlsx"
USERS = 'users'
PRODUCTS = 'products'
ORDERS = 'orders'


with open(CONFIG_PATH + USERS + '.csv','r') as f:
    values = []
    data = csv.reader(f)
    for row in data:
        values.append(tuple(row))
    sql =  """
    insert into users (user_id,user_name, user_email, user_password, user_address, is_vendor)
    values ("%s,%s,%s,%s,%s,%s")
    """
    values.pop(0)
    db.insert_many_records(connection,sql,values)
print("Data insertion in User Table completed")
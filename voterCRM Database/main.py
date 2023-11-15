# pip install mysql-connector-python streamlit
# pip install mysql-connector-python
from datetime import datetime, timedelta
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

class User:
    def __init__(self, user_ID,user_role,subscription_type,subscription_status):
        self.user_id = user_ID
        self.user_role = user_role
        self.susbscription_type = subscription_type
        self.susbscription_status = subscription_status

# Function to perform an action based on user role
def perform_action_based_on_role(user):
    if user.user_role == 'Admin':
        print("Admin can perform this action")
    else:
        print("This action is not allowed for non-admin users.")

# Function to perform an action based on subscription type
def perform_action_based_on_subscription(user):
    if user.subscription_type == 'Individual':
        print("Individual subscription user can perform this action.")
        # Perform premium-specific action
    else:
        print("This action is not allowed for group subscription users.")

def perform_action_based_on_subscription_status(user):
    if user.subscription_status == 'Active':
        print("User has an active subscription. Performing action...")
    elif user.subscription_status == 'Pending':
        print("User has a pending subscription. Cannot perform the action yet.")
    elif user.subscription_status == 'Cancelled':
        print("User's subscription is cancelled. Action not allowed.")
    elif user.subscription_status == 'Expired':
        print("User's subscription has expired.")

def fetch_voter_data():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(" SELECT * FROM VOTER")
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return []


def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

if __name__ == "__main__":
    connection = create_server_connection()
    create_and_switch_database(connection, database, database)
    create_table(connection, create_voter_table)

    # Fetch voter data
    voters_data = fetch_voter_data(connection)

    # Perform actions for each user (admin, candidate, party worker)
for user_data in users_data:
    user = User(user_ID=user_data['User_ID'], 
                user_role=user_data['User_Role'], 
                subscription_type='Individual', 
                subscription_status='Active')
    # Check if the user has a valid role
    if user.user_role in ('Admin', 'Candidate', 'Party_worker'):
        # Perform actions based on user roles, subscription types, and subscription status
        perform_action_based_on_role(user)
        perform_action_based_on_subscription(user)
        perform_action_based_on_subscription_status(user)
    else:
        print(f"Skipping actions for user {user.user_id} with role {user.user_role}")
   
    close_connection(connection)

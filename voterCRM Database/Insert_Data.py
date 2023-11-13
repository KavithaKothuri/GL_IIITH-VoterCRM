import csv
import pandas as pd
from sqlconnection import connection, cursor


# Read data from the CSV file into a DataFrame
csv_file = "voterCRM_sample_data.csv"
data = pd.read_csv(csv_file)

# Function to insert data from a CSV file into a table
def insert_data_from_csv(csv_filename, table_name):
    with open(csv_filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row if it exists in your CSV file
        for row in csv_reader:
            # Define your SQL INSERT statement
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(insert_query, row)
            print("Data insertion completed")
            

# Insert data into each table
insert_data_from_csv('voterCRM_sample_data.csv', 'USERS')
insert_data_from_csv('voterCRM_sample_data.csv', 'VOTER')
insert_data_from_csv('voterCRM_sample_data.csv', 'ADDRESS')
insert_data_from_csv('voterCRM_sample_data.csv', 'CONTACT')
insert_data_from_csv('voterCRM_sample_data.csv', 'FAMILY')
insert_data_from_csv('voterCRM_sample_data.csv', 'RELIGION')
insert_data_from_csv('voterCRM_sample_data.csv', 'POLITICAL_AFFILIATION')
insert_data_from_csv('voterCRM_sample_data.csv', 'POLICE_CASE')


# Commit the changes and close the connection
connection.commit()
connection.close()

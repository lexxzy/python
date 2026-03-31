import pyodbc 
import os
import pandas as pd 
#import numpy as np 
from dotenv import load_dotenv 

# DataBase Creds for SQL DB
SERVER_HOST = r'localhost\SQLEXPRESS'
DATABASE_NAME = 'EmployeesDB'
CONNECTION_ID = 'yes'
CERTIFICATE_ID = 'yes'

load_dotenv()


'''
SERVER_HOST = r'localhost\SQLEXPRESS'
DATABASE_NAME = 'EmployeesDB'
CONNECTION_ID = 'yes'
CERTIFICATE_ID = 'yes'

'''


connectionString = f"""
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={SERVER_HOST};
DATABASE={DATABASE_NAME};
Trusted_Connection={CONNECTION_ID};
Encrypt={CERTIFICATE_ID};
TrustServerCertificate={CERTIFICATE_ID};
"""








# Connect to SQL database using pyodbc 
'''
connectionString = f"""
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={DB_HOST};
DATABASE={DB_NAME};
Trusted_Connection={DB_CONNECTION_ID};
Encrypt={DB_CERTIFICATE_ID};
TrustServerCertificate={DB_CERTIFICATE_ID};
"""


'''


conn = pyodbc.connect(connectionString)



# quick query of data table and printout
QUERY = '''SELECT id_num, fname, lname, age, salary FROM emp_db_owner.employees'''
cursor = conn.execute(QUERY)
records = cursor.fetchall()

# Print I
for r in records:
    print(f"{r.id_num}\t{r.fname}\t{r.lname}\t{r.age}\t{r.salary}")

# Use List Array
employees_list = []
employees_list = records

# <<>> Sort Descending
employees_list.sort(reverse=True)

# Print II
print("")
for data in employees_list:
    print(data.id_num, data.fname, data.lname, data.age, data.salary, sep=' ')



#<------------------ Using Pandas DataFrame ----------------------> 

#Read Data from Database
stmt = "SELECT * FROM emp_db_owner.employees"

#Pandas Read_sql" feature Print
#Pandas "head" feature below fetches first 10 rows
df = pd.read_sql(stmt,conn)
df.head(10)

print('') #prints empty line to create space btw results
print(df)

''' -----------/\/\/\/\/\----------- '''

#--- **** NEW SCRIPT - USING PANDAS DATA FRAME *****

#SQL Statement to Read Data from Database
stmt = "SELECT * \
        FROM emp_db_owner.employees \
        WHERE age >= 30 \
        AND fname NOT LIKE 'A%'"

# Perform use of Pandas DataFrame
df = pd.DataFrame(pd.read_sql(stmt,conn))
print('') # prints empty line

# Check if data was retrieved
# If-else checks if query returned results
if not df.empty:
    print("\nEmployee Records Retrieved:")
    print(df) # Prints the DataFrame result
else:
    print("\nNo matching records found.")


''' -----------/\/\/\/\/\----------- '''

#--- **** NEW SCRIPT - INSERT NEW DATA TO SQL DATABASE *****

# Step 1: create table in SSMS using below:

'''CREATE TABLE emp (
    firstname VARCHAR(20),
    lastname VARCHAR(20)
);'''

# Step 2: The below inserts new data rows into the a SQL Database table emp.
# the 'try-except' block catches & handle errors, preventing script crashes,
# by allowing alternative actions when exceptions occur!

try:
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO emp VALUES (?, ?)",
        [
            ('x-men III', '2012'),
            ('avengers', '2019')
        ]
    )
# Commit the transaction
    conn.commit()
    print("Records inserted successfully!")

 # Handle Database errors
except pyodbc.DatabaseError as db_err:
    print(f"Database error occurred: {db_err}")
    conn.rollback()  

 # Handle Python/script errors
except Exception as e:
    print(f"An error occurred: {e}")

 # Close the connection
finally:
    cursor.close()
    conn.close()
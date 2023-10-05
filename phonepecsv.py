import csv
# Creating connection with MySQL
# Connecting with SQL
import mysql.connector as sql
mydb = sql.connect(host="localhost", #127.0.0.1
                   user="root",
                   password="0000000000000000000000000",
                   port="3306",
                   database= "phonepe_pulse",
                   auth_plugin="mysql_native_password"
                  )
mycursor = mydb.cursor(buffered=True)
h = '3306' #3307

# CSV file path
csv_file_path = r'D:\phonepeproject\top_trans.csv'
# Specify the target table name in your database
table_name = 'top_trans'

# Establish database connection
conn = sql.connect(host="localhost", user="root", password="Adrielsheena@03", database="phonepe_pulse", port=3306)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Read CSV file and insert data into the database
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Read the header to get column names

    # Create the SQL query with placeholders for column names
    columns = ', '.join(header)
    placeholders = ', '.join(['%s'] * len(header))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Loop through the rows in the CSV and execute the insert query
    for row in csv_reader:
        cursor.execute(insert_query, row)

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()

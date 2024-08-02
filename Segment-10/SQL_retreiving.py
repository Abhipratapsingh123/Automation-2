import mysql.connector

db_config = {
    'user': 'root',
    'password': 'Abhi.',
    'host': '127.0.0.1'
}

# Establish a connection to the MySQL database
con = mysql.connector.connect(**db_config)

# Check if the connection is successful
if con.is_connected():
    print("Connection established successfully.")
else:
    print("Failed to establish connection.")

# Print connection object
print(con)

# Don't forget to close the connection when done
con.close()

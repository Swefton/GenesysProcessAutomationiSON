import mysql.connector

# Database connection parameters
db_config = {
    'user': 'Aws_reporting',
    'password': '!$0ngl0bal@SQ1_Us4r2',
    'host': 'your_database_host',
    'database': 'your_database_name',
}

# Establish a connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read and upload data from a local CSV file
with open('data.csv', 'r') as file:
    next(file)  # Skip header line if needed
    for line in file:
        values = line.strip().split(',')
        # Customize this query based on your table structure
        query = f"INSERT INTO your_table_name (column1, column2, ...) VALUES (%s, %s, ...)"
        cursor.execute(query, values)
        connection.commit()

# Close the connection
cursor.close()
connection.close()
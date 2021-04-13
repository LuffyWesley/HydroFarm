import pyodbc
import keys

# Un-comment the next two lines below if running code on Raspberry Pi
# connString = 'DSN={0};UID={1};PWD={2};DATABASE={3};'.format(keys.dsn,keys.user,keys.password,keys.database)
# conn = pyodbc.connect(connString)

# Un-comment the line below if running code on Mac/PC
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+keys.server+';DATABASE='+keys.database+';UID='+keys.user+';PWD='+ keys.password)

cursor = conn.cursor()

# Drop previous table of same name if one exists
# cursor.execute("DROP TABLE IF EXISTS test;")
# print("Finished dropping table (if existed).")

# Create table
# cursor.execute("CREATE TABLE test (speech NVARCHAR(MAX), neg FLOAT(53), color VARCHAR(50), creationTime smalldatetime)")
# print("Finished creating table.")

# Insert some data into table
cursor.execute("INSERT INTO test (speech, neg, color, creationTime) VALUES (?, ?, ?, GETDATE());", ("dragon", "69.420", "pink"))
print("Inserted",cursor.rowcount,"row(s) of data.")

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")
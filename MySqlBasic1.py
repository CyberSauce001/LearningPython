import pymysql

servername = "localhost";
username = "root";
password = "";
dbname = "";

db = pymysql.connect(servername, username, password, dbname)

cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS automated_test")

# Create table as per requirement
sql = """CREATE TABLE automated_test (
   Scripts  CHAR(50),
   Conditons  CHAR(20), 
   Date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"""

cursor.execute(sql)
db.close()

#!/usr/bin/python
"""
Ref: https://www.tutorialspoint.com/python/python_database_access.htm
On Ubuntu16.04
# apt-get install build-essential python-dev libapache2-mod-wsgi-py3 libmysqlclient-dev
# pip install MYSQL-python

"""

import MySQLdb

# 1. Open database connection
db = MySQLdb.connect("localhost","root","default","test_db");

# 2. prepare a cursor object using cursor() method
cursor = db.cursor()

# 3. execute SQL query using execute() method.
cursor.execute("SELECT * from task;")

# 4. fetch data
print cursor.fetchall()

# sql = """CREATE/INSERT/UPDATE/DELETE"""
# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Commit your changes in the database
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# 5. disconnect from server
db.close()


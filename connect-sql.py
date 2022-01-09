import pandas as pd 
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',database='titanic',user='root', password='', use_pure=True)

qry = 'select * from mytable'
db = pd.read_sql(qry, connection)
print(db)
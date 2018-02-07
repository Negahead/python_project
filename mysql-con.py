import mysql.connector

cnx = mysql.connector.connect(user='me', password='2b172b', host='127.0.0.1', database='will')
if cnx.is_connected():
    pass
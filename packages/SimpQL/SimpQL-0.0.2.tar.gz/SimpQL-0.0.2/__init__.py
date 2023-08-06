import mysql.connector

connection = None
cursor = None

def initialise(dbHost, dbUser, dbPassword, dbName):
	"""
		Initialises the connection to the database.
	"""

	global connection, cursor

	connection = mysql.connector.connect(
		host = dbHost,
		user = dbUser,
		password = dbPassword,
		database = dbName
	)

	cursor = connection.cursor()

def select_all(table, where = None):
	"""
		Selects all values in 'table'
	"""
	if where == None:
		where = ""
	else:
		where = " WHERE " + where

	print(f"SELECT * FROM {table}{where}")
	cursor.execute(f"SELECT * FROM {table}{where}")
	return cursor.fetchall()
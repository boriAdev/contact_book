import sqlite3
from sqlite3 import Error

'''CONNECTING TO DATABASE '''

def create_connection(db_file):

	''' CREATING CONNECTION TO sqlite3 DATABASE '''
	conn = None

	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)

	finally:
		if conn:
			print("DATABASE CREATION SUCESSFUL!")
		else:
			print("DATABASE CREATION FAILED!")
		return conn

'''CREATING DATABASE '''

def create_table():

	conn = create_connection('C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
	c = conn.cursor()

	create_table_command = """
	CREATE TABLE IF NOT EXISTS
	contacts(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, phone_no INTEGER, email TEXT)
	"""
	c.execute(create_table_command)
	conn.close()

# def insert_into_DB(first_name,last_name, phone_no, email_add):
#     conn = create_connection('C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
#     # sql_insert = """ INSERT INTO contacts(firstname, lastname, phone_no, email) VALUES(?,?,?,?),
# 	# (first_name, last_name, phone_no, email_add) """
#     c = conn.cursor()
#     # c.execute(sql_insert)
# 	c.execute("INSERT INTO contacts(firstname, lastname, phone_no, email) VALUES(?,?,?,?)", (first_name, last_name, phone_no, email_add))
#     conn.commit()
#     conn.close()

def insert_into_DB(first_name, last_name, phone_no, email_add):
	conn = create_connection('C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
	c = conn.cursor()
	c.execute("INSERT INTO contacts(firstname, lastname, phone_no, email) VALUES(?,?,?,?)", (first_name, last_name, phone_no, email_add))
	conn.commit()
	conn.close()

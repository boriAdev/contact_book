import sqlite3
from sqlite3 import Error

'''OPERATIONAL FUNCTIONS '''
class Contacts():

	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.phone_no = None
		self.email_add = None

	''' METHOD TO CREATE CONTACT'''

	def create_new_contact(self, fname, lname, phonenumber, emailaddress):

		self.first_name = fname
		self.last_name = lname
		self.phone_no = phonenumber
		self.email_add = emailaddress

		# cursor.execute("INSERT INTO contacts VALUES(self.first_name, self.last_name, self.phone_no,  self.email_add)")

	'''LIST ALL CONTACTS'''
	
	def show_all_contacts(self):
		cursor.execute("SELECT * FROM contacts")
		results = cursor.fetchall()
		print(results)

'''CONNECTING TO DATABASE '''

def create_connection(db_file):
	''' CREATING CONNECTION TO sqlite3 DATABASE '''
	conn = None

	try:
		com = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)

	finally:
		if conn:
			conn.close()

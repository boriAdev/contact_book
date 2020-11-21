import sqlite3
from sqlite3 import Error
from db_conn import *

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

		insert_into_DB(fname, lname, phonenumber, emailaddress)


	'''LIST ALL CONTACTS'''

	def show_all_contacts(self):
		c.execute("SELECT * FROM contacts")
		results = c.fetchall()
		print(results)

	'''UPDATEING A CONTACT '''
	def update_contact(self):
		pass

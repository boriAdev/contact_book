import sqlite3
import __init__

'''Contains functional '''
class Contacts():

	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.phone_no = None
		self.email_add = None

	''' Method to create contact'''

	def create_new_contact(self, fname, lname, phonenumber, emailaddress):

		self.first_name = fname
		self.last_name = lname
		self.phone_no = phonenumber
		self.email_add = emailaddress

		cursor.execute("INSERT INTO contacts VALUES(self.first_name, self.last_name, self.phone_no,  self.email_add)")

	def show_all_contacts(self):
		cursor.execute("SELECT * FROM contacts")
		results = cursor.fetchall()
		print(results)

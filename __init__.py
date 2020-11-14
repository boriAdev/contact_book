''' Contact Book Application'''
from contact_book import Contacts
import sqlite3

if __name__=="__main__":

	# CREATE AND CONNECT TO DATABASE
	connection = sqlite3.connect('phonebook.db')
	cursor = connection.cursor()

	create_table_command = """
	CREATE TABLE IF NOT EXISTS
	contacts(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, phone_no INTEGER, email TEXT)
	"""
	cursor.execute(create_table_command)

	'''Application Interface'''

	on = True
	while on:
		print("-------Contact Book----------")
		print("Choose an option:")
		print("C - Create New Contact")
		print("U - Update a contact")
		print("D - Delete a Contact")
		print("L - List Contact")
		print("B - Backup contacts in the Cloud")
		print("Q - Quit")

		starter =input(' : ')

		''' If user selects C to create contact'''

		if starter.upper() =='C':

			# USER INPUT
			fname = input('Enter First Name: ')
			lname = input('Enter Last Name: ')
			phonenumber = input('Enter Phone Number: ')
			emailaddress = input('Enter Email Address: ')

			# CREATE NEW CONTACT
			new_contact = Contacts()
			new_contact.create_new_contact(fname,lname,phonenumber,emailaddress)
			# print(new_contact.first_name)


		'''User ends Application'''

		if starter.upper() == "Q":
			on = False

''' Contact Book Application'''
from contact_book import Contacts

if __name__=="__main__":

	'''CREATING DATABASE '''
	# create_connection('C:\Users\boria\Documents\Python Scripts\contact_book\contacts.db')
	#
	# conn.open()
	# create_table_command = """
	# CREATE TABLE IF NOT EXISTS
	# contacts(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, phone_no INTEGER, email TEXT)
	# """
	# conn.execute(create_table_command)
	# conn. close()

	'''APPLICATION INTERFACE'''

	# while loop that starts the application
	on = True
	while on:
		print("-------CONTACT BOOK----------")
		print("Choose an option:")
		print("C - Create New Contact")
		print("U - Update a contact")
		print("D - Delete a Contact")
		print("L - List Contact")
		print("B - Backup contacts in the Cloud")
		print("Q - Quit")

		starter =input(' : ')
		while starter.upper() not in ['C','U','D','L','B','Q']:
			try:
				starter =input(' : ')
			except:
				print("invalid input. Try again")

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


		'''USER ENDS APPLICATION'''

		if starter.upper() == "Q":
			on = False

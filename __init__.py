''' Contact Book Application'''
from contact_book import *
from db_conn import *
import sqlite3


if __name__=="__main__":

	''' CREATING CONNECTION TO DATABASE THEN TABLE'''
	create_table()

	'''APPLICATION INTERFACE'''
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

		starter =input(' Enter Input Here: ')

		''' USER SELECTS C TO CREATE A NEW CONTACT'''

		if starter.upper() =='C':
			# USER INPUT
			fname = input('Enter First Name: ')
			lname = input('Enter Last Name: ')
			phonenumber = input('Enter Phone Number: ')
			emailaddress = input('Enter Email Address: ')

			# CREATE NEW CONTACT
			new_contact = Contacts()
			new_contact.create_new_contact(fname,lname,phonenumber,emailaddress)

			while True:
				more = input("Do you want to perform another function? (Y/N): ")
				# keep_going = True
				if more.upper() == "Y":
					break
				elif more.upper() == "N":
					print('APPLICATION END!')
					on = False
					break
				else:
					print('Wrong input, try again')



		if starter.upper() =='L':
			pass

		'''USER ENDS APPLICATION'''

		if starter.upper() == "Q":
			on = False



		# '''USER ENDS APPLICATION'''

	# elif starter.upper() == "Q":
	# 		on = False

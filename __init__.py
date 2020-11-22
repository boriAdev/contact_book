''' CONTACT BOOK APPLICATION'''
from contact_book import *
from db_conn import *
import sqlite3


if __name__=="__main__":

	''' CREATING AND CONNECTING TO DATABASE THEN TABLE'''
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

		while starter.upper() not in {"C":"C", "U":"U", "D":"D", "L":"L", "B":"B", "Q":"Q"}:
			print("INVALID INPUT, PLEASE TRY AGAIN")
			break

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
				if more.upper() == "Y":
					break
				elif more.upper() == "N":
					print('APPLICATION END!')
					on = False
					break
				else:
					print('Wrong input, try again')

		'''USER WANTS TO UPDATE A SAVED CONTACT'''

		if starter.upper() =='U':
			
			'''FUNCTION TO BE PERFORMED'''


			'''LOGIC CONTINUATION'''

			while True:
				more = input("Do you want to perform another function? (Y/N): ")
				if more.upper() == "Y":
					break
				elif more.upper() == "N":
					print('APPLICATION END!')
					on = False
					break
				else:
					print('Wrong input, try again')


		'''USER WANTS TO DELETE EXISTING CONTACT'''

		if starter.upper() =='D':

			'''FUNCTION TO BE PERFORMED'''


			'''LOGIC CONTINUATION'''
			
			while True:
				more = input("Do you want to perform another function? (Y/N): ")
				if more.upper() == "Y":
					break
				elif more.upper() == "N":
					print('APPLICATION END!')
					on = False
					break
				else:
					print('Wrong input, try again')


		''' USER WANTS TO VIEW ALL CONTACTS'''

		if starter.upper() =='L':
			
			'''FUNCTION TO BE PERFORMED'''


			'''LOGIC CONTINUATION'''
			
			while True:
				more = input("Do you want to perform another function? (Y/N): ")
				if more.upper() == "Y":
					break
				elif more.upper() == "N":
					print('APPLICATION END!')
					on = False
					break
				else:
					print('Wrong input, try again')


		'''USER WANTS TO BACKUP A CONTACT LIST TO THE CLOUD'''

		if starter.upper() =='L':
			
			'''FUNCTION TO BE PERFORMED'''


			'''LOGIC CONTINUATION'''
			
			while True:
				more = input("Do you want to perform another function? (Y/N): ")
				if more.upper() == "Y":
					break
				elif more.upper() == "N":
					print('APPLICATION END!')
					on = False
					break
				else:
					print('Wrong input, try again')
		

		'''USER ENDS APPLICATION'''

		if starter.upper() == "Q":
			on = False
